import uuid
import requests
from typing import Optional, Dict, Any

# langchain 
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool

from pydantic import BaseModel, Field, field_validator

DEFAULT_BASE_URL = "http://localhost:5000/~/id-in/cse-in"
DEFAULT_ORIGIN = "CArt"

class OneM2MRequestInput(BaseModel):
    method: Optional[str] = Field(default="GET", description="HTTP method (GET, POST, PUT, DELETE). Defaults to GET.")
    url: Optional[str] = Field(default=DEFAULT_BASE_URL, description="Target oneM2M resource URL. Defaults to IN-CSE base URL.")
    origin: Optional[str] = Field(default=DEFAULT_ORIGIN,description="X-M2M-Origin. Defaults to CAdmin.")
    resource_type: Optional[int] = Field(default=None, description="oneM2M resource type (ty). Inferred if missing.")
    payload: Optional[Dict[str, Any]] = Field(default=None, description="oneM2M JSON payload. Auto-generated if missing.")

    @field_validator("method")
    def normalize_method(cls, v):
        return v.upper()


@tool(args_schema=OneM2MRequestInput)
def oneM2MExecuteRest(method, url, origin, resourceType, payload):
    """Perform oneM2M HTTP REST operations (GET, POST, PUT, DELETE) 
        on ACME CSE using standard headers."""    
    headers = {
        "X-M2M-Origin": origin,
        "X-M2M-RI": str(uuid.uuid4()),
        "Accept": "application/json",
    }
    if method.upper() == "POST":
        headers["Content-Type"] = (f"application/json;ty={resourceType}" if resourceType else "application/json")
    elif method.upper() == "PUT":
        headers["Content-Type"] = (f"application/json")
    try:
        response = requests.request(method=method.upper(), url=url, headers=headers,json=payload, timeout=10)
        return (
            f"Status: {response.status_code}\n"
            f"Response:\n{response.text}"
        )
    except Exception as e:
        return f"oneM2M REST request failed: {str(e)}"


