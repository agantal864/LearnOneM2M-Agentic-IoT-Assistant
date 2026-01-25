from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from pydantic import BaseModel, Field
from typing import Literal


validTypes = Literal[
    "concept", "resource_type_info", "short_names",
    "mandatory_attributes", "optional_attributes",
    "procedures", "behavior", "constraints",
    "security", "relationship", "example_payload",
    "table_of_contents",
    "references",
    "non_qa_content"
]

class qaType(BaseModel):
    q: str = Field(..., description=(
            "The question derived from the content. "
            "If the content is not a question-answerable section "
            "(e.g., table of contents, references, index), "
            "use 'N/A - non-question content'."
            ))
    a: str = Field(...,  description=(
            "The answer to the question. "
            "If no answer exists because the content is structural "
            "(e.g., table of contents or references), "
            "use 'N/A - non-question content'."
            ))
    type: str = Field(..., description="Category of the Q&A")
    section_metadata: str = Field(..., description="Given section metadata")

sysPrompt = f"""
    You are a technical oneM2M expert. 

    REQUIREMENTS:
    - If you find technical rules (e.g., "X-M2M-RI header is mandatory"), create a chunk.

"""
MODEL = "gpt-oss:20b" 
metadata = "{'Header 3': 'Method'}"
pageContent = """
The HTTP ‘Method’ shall be derived from the Operation request primitive parameter of the request primitive.

Table 6.2.1-1: HTTP Method Mapping

At the Receiver, an HTTP request message with POST method shall be mapped either to a Create or Notify Operation parameter. Discrimination between Create and Notify operations can be accomplished by inspection of the content-type header. The Resource Type parameter is present in the content-type header only when the HTTP POST request represents a Create request (see clause 6.4.3). The Resource Type parameter is not present in the content-type header when the HTTP POST request represents a Notify request.

"""

llm = ChatOllama(model=MODEL, temperature=0) 

structured_llm = llm.with_structured_output(qaType)
result = structured_llm.invoke(f"""
Extract facts and turn them into Question/Answer pairs.
Analyze this section metadata from the technical specification: {metadata}

TEXT TO ANALYZE:
{pageContent}
""")

print(result)
