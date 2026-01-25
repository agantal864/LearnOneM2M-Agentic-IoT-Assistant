import os
import json
import time
# Schema
from pydantic import BaseModel, Field
from typing import List
# Langchain
from langchain_ollama import ChatOllama
# Langchain text splitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Chroma
import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "TS-0009-HTTP_Protocol_Binding_Specifications"
MODEL = "llama3.1:latest" 
target_spec = "rawData/specifications/TS-0009-HTTP_Protocol_Binding-V3_9_1(cl).md"

# Structured LLM output Schema
class qaType(BaseModel):
    q: str = Field(..., description="The technical question derived from the content.")
    a: str = Field(..., description="The detailed answer to the question.")
    category: str = Field(..., description="Category of the Q&A (e.g., Security, Mapping, Headers)")
# List of generated Q&A per section (Schema)
class qaList(BaseModel):
    pairs: List[qaType] = Field(..., description="A list of extracted Question/Answer pairs")

# Function to split markdown text by headers
def textSplit(file_path):
    # Read .md file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Markdown header text splitting
    headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdown_splitter  = MarkdownHeaderTextSplitter(headers_to_split_on)
    md_header_splits  = markdown_splitter.split_text(content)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    final_splits = text_splitter.split_documents(md_header_splits)
    ExtractedQA = []
    staging_file = f"refined_{os.path.basename(file_path)}.json"

    for i, section in enumerate(final_splits):
        # Add metadata to every section.page_content (Default: General)
        metadata = section.metadata if section.metadata else {"Header": "General"}
        # Refine content and metadata with LLM
        result = refine(metadata, section.page_content)
        # Filter N/A question pairs
        filteredResults = [p for p in result.pairs if p.q.upper() != "N/A"]
        
        # Add source filename to output 
        for result in filteredResults:
            pairDict = result.model_dump() 
            # Inject the source filename
            pairDict['section_metadata'] = metadata
            pairDict['source'] = os.path.basename(file_path)
            # Add to master list
            ExtractedQA.append(pairDict)

        if i % 5 == 0:
            with open(staging_file, 'w', encoding='utf-8') as f:
                json.dump(ExtractedQA, f, indent=2, ensure_ascii=False)
        # add pause         
        time.sleep(1)

    with open(staging_file, 'w', encoding='utf-8') as f:
        json.dump(ExtractedQA, f, indent=2, ensure_ascii=False)

    print(f"--- Refinement Complete. Saved {len(ExtractedQA)} chunks to {staging_file} ---")

# Function to refine chunks using LLM
def refine(metadata: str, pageContent: str) -> qaList:
    """Uses LLM to extract multiple technical facts into structured Q&A pairs."""
    llm = ChatOllama(model=MODEL, temperature=0)  
    structured_llm = llm.with_structured_output(qaList)
    prompt = f"""
        You are a strict technical oneM2M expert.

        TASK:
        Extract all technical facts from the text below and 
        format them as a list of Question/Answer pairs.
        
        SECTION METADATA: {metadata}
        TEXT TO ANALYZE:
        {pageContent}
        
        CRITICAL RULES:
        1. If the text to analyze is just a Table of Contents, References, or boilerplate, 
        return: q='N/A', a='N/A', category='N/A'.
        2. NO META-DATA extraction: Do not create questions about these instructions or the 'N/A' rule.
        3. NO HALLUCINATION: If the text is just a Table of Contents or a list of headers without descriptions, return q='N/A'.
        4. BE SPECIFIC: Focus on binding details: methods, header fields, and status code mappings.
        5. DATA SOURCE: Only use information provided in the "TEXT TO ANALYZE" block.
        6. Focus on specific technical details (e.g., HTTP methods, status codes, header fields).
        7. NO POINTERS: Do not provide answers that only point to tables, clauses, or figures (e.g., "See Table 6.3.2-1"). 
            - If the text is a table, extract the specific rows into individual Q&A pairs.
            - Example: q="What is the HTTP Status for oneM2M code 2001?", a="201 Created".
        """
    return structured_llm.invoke(prompt)


if __name__ == "__main__":
    # Setup Chroma, llm, and embedding function
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="BAAI/bge-small-en-v1.5"
    )
    spec_col = client.get_or_create_collection(COLLECTION_NAME, embedding_function=embedding_func)
    staging_path = textSplit(target_spec)