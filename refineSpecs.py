import os
import json
import time
import re
import difflib
# Schema
from pydantic import BaseModel, Field
from typing import List
# Langchain
from langchain_ollama import ChatOllama
# Langchain text splitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


MODEL = "llama3.1:latest" 
INPUT_DIR = "rawData/specifications"
OUTPUT_DIR = "rawData/specifications/processed"

# Structured LLM output Schema
class qaType(BaseModel):
    q: str = Field(..., description="The technical question derived from the content.")
    a: str = Field(..., description="The detailed answer to the question.")
    category: str = Field(..., description="Category of the Q&A (e.g., Security, Mapping, Headers)")

# List of generated Q&A per section (Schema)
class qaList(BaseModel):
    pairs: List[qaType] = Field(..., description="A list of extracted Question/Answer pairs")


def textSplitAndRefine(filePath):
    """Split markdown text by headers + Refining with LLM"""

    # Naming 
    baseName = os.path.basename(filePath)
    jsonFilename = "refined_" + baseName.rsplit('.', 1)[0] + ".json"

    # Read .md file
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Markdown header text splitting
    headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdown_splitter  = MarkdownHeaderTextSplitter(headers_to_split_on)
    md_header_splits  = markdown_splitter.split_text(content)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    final_splits = text_splitter.split_documents(md_header_splits)

    # Refining
    ExtractedQA = []
    for section in final_splits:
        # Add metadata to every section.page_content (Default: General)
        metadata = section.metadata if section.metadata else {"Header": "General"}
        # Refine content and metadata with LLM
        result = refine(metadata, section.page_content)
        # Filter N/A question pairs
        filteredResults = [p for p in result.pairs if p.q.upper() != "N/A"]   
        # Add source filename to output 
        for res in filteredResults:
            pairDict = res.model_dump() 
            # Inject the source filename
            pairDict['section_metadata'] = metadata
            pairDict['source'] = os.path.basename(filePath)
            # Add to master list
            ExtractedQA.append(pairDict)
        time.sleep(1)

    print(f"\nProcessed: {jsonFilename}")
    return ExtractedQA

# Function to refine chunks using LLM
def refine(metadata: str, pageContent: str) -> qaList:
    """Uses LLM to extract multiple technical facts into structured Q&A pairs."""

    # Initialize LLM with structured output
    llm = ChatOllama(model=MODEL, temperature=0, num_predict=4096, num_ctx=8192)  
    structured_llm = llm.with_structured_output(qaList)
    prompt = f"""
        You are a technical oneM2M expert. 
        TASK:
        Extract all technical facts related to the oneM2M standard from the text below and 
        format them as a list of Question/Answer pairs.
        CONSTRAINTS:
        1. If the text to analyze is just a Table of Contents, References, or boilerplate, 
        return: q='N/A', a='N/A', category='N/A'. 
        2. NO META-DATA extraction: Do not create questions about these instructions or the 'N/A' rule.
        3. NO HALLUCINATION: If the text is just a Table of Contents or a list of headers without descriptions, return q='N/A'.
        Example:
        Text to analyze: "Contents 1 Scope 14, 2 References 14..." (this is a table of contents)
        return q='N/A' a = 'N/A' 
        4. BE SPECIFIC: Focus on specific technical details (e.g., HTTP methods, status codes, header fields). Don't create qa pairs related to the structure of the document. 
        Correct Example: 
            "q": "What are the components of an HTTP request message?",
            "a": "Request-Line, headers and message-body."
        Wrong Example:
            "q": "What is the section about Message Routing?",
            "a": "6.6Message Routing19"
        5. DATA SOURCE: Only use information provided in the "TEXT TO ANALYZE" block. Treat this text as the only source of truth. 
        6. EXHAUSTIVE EXTRACTION: If a table is present, you MUST create a Q&A pair for 
            EVERY row in that table. Do not summarize or skip rows.
        7. NO TRUNCATION: Do not stop until every technical fact is converted.
        CRITICAL CONSTRAINT:
        8. NO POINTERS: Do not provide answers that only point to tables, clauses, or figures (e.g., "See Table 6.3.2-1"). 
            - If the text is a table, extract the specific rows into individual Q&A pairs.
            - Example: q="What is the HTTP Status for oneM2M code 2001?", a="201 Created".
            - If the definition is not in the current text, skip the question.
            - Correct Example: Q: What is the supported HTTP version? A: HTTP 1.1.
            - Wrong Example: Q: Where is versioning? A: Clause 6
        SECTION METADATA: {metadata}
        TEXT TO ANALYZE:
        {pageContent}
        """

    return structured_llm.invoke(prompt)


def cleanRefinedJson(data):
    """
    Filters out duplicates, N/A responses, and pointers to clauses/tables.
    Specifically targets 'SectionTopicPage' noise.
    """
    uniquePairs = {}
    initialCount = len(data)
    # Broad patterns for 'useless' answers
    forbiddenPatterns = [
        r"see\s+clause", r"refer\s+to", r"table\s+\d", 
        r"clause\s+\d", r"section\s+\d", r"n/a", r"not\s+specified",
        r"as\s+described\s+in"
    ]
    # Pattern for "7.2Transport Layer Security19"
    sectionPagePattern = r"^\d+[\d\.]*[A-Z][a-zA-Z\s\-\_]+\d+$"

    for entry in data:
        qText, aText = entry['q'].strip(), entry['a'].strip()
        
        # 1. Length & N/A Filter
        if qText.upper() == "N/A" or aText.upper() == "N/A":
            continue
            
        # 2. Forbidden Phrases Filter
        if any(re.search(pat, aText, re.IGNORECASE) for pat in forbiddenPatterns):
            continue

        # 3. Section-Page Noise Filter (The '7.2Security19' issue)
        if re.match(sectionPagePattern, aText.replace(" ", "")):
            continue

        # 4. Fuzzy Filter: Remove circular Q&A (Question and Answer too similar)
        similarity = difflib.SequenceMatcher(None, qText.lower(), aText.lower()).ratio()
        if similarity > 0.85:
            continue

        # 5. Deduplication and Category Normalization
        # Using (Question + Answer) as the key to catch duplicates
        key = (qText.lower(), aText.lower())
        if key not in uniquePairs:
            entry['q'], entry['a'] = qText, aText
            # Normalize Category (e.g., "Onem2M Standard" vs "Onem2m Standard")
            if 'category' in entry:
                entry['category'] = entry['category'].strip().title()
            uniquePairs[key] = entry

    cleanedData = list(uniquePairs.values())

    print(f"--- Cleaning Complete ---")
    print(f"Removed: {initialCount - len(cleanedData)} pairs")
    print(f"Remaining: {len(cleanedData)}")
    return cleanedData

def batchProcess(inputFolder, outputFolder):
    """Iterates through all markdown files in a folder."""
    os.makedirs(outputFolder, exist_ok=True)
    
    files = [f for f in os.listdir(inputFolder) if f.endswith('.md')]
    print(f"Found {len(files)} files to process.")

    for filename in files:
        inputPath = os.path.join(inputFolder, filename)
        outputFile = os.path.join(outputFolder, f"refined_{filename.rsplit('.', 1)[0]}.json")

        if os.path.exists(outputFile):
            print(f"Skipping {filename}, already exists.")
            continue

        rawQa = textSplitAndRefine(inputPath)
        cleanedQa = cleanRefinedJson(rawQa)
        
        with open(outputFile, 'w', encoding='utf-8') as f:
            json.dump(cleanedQa, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully saved {len(cleanedQa)} pairs to {outputFile}")

if __name__ == "__main__":
    batchProcess(INPUT_DIR, OUTPUT_DIR)