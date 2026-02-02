# LangSmith Tracing
from dotenv import load_dotenv
load_dotenv()

import uuid
import requests
from typing import Optional, Dict, Any

# langchain 
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from pydantic import BaseModel, Field, field_validator


agentModel = ChatOllama(model="gpt-oss:20b", temperature=0, num_ctx=32768, num_predict=-1)

DEFAULT_BASE_URL = "http://localhost:5000/~/id-in/cse-in"
DEFAULT_ORIGIN = "CAdmin"

class OneM2MRequestInput(BaseModel):
    url: Optional[str] = Field(default="http://localhost:5000/~/id-in/cse-in", description="Base URL of the ACME CSE (Common Services Entity) where resources will be created and accessed. All AE, CNT, CIN, SUB, and other resource operations use this as the root URL.")
    method: Optional[str] = Field(default="GET", description="HTTP method (GET, POST, PUT, DELETE). Defaults to GET.")
    origin: Optional[str] = Field(default=DEFAULT_ORIGIN,description="X-M2M-Origin. For AE registration, this MUST be a new unique ID (e.g., 'CMyApp'). For other tasks, use 'CAdmin' if origin is not given in the query.")
    resourceType: Optional[int] = Field(default=None, description="oneM2M resource type (ty). Inferred if missing.")
    payload: Optional[Dict[str, Any]] = Field(default=None, description="oneM2M JSON payload. The payload must comply with the ACME CSE requirements. If not supplied from user query, generate a valid payload. If lacking, complete the payload to make it valid.")

    @field_validator("method")
    def normalize_method(cls, v):
        return v.upper()

@tool(args_schema=OneM2MRequestInput)
def OneM2MRequest(url, method, origin, resourceType, payload):
    """Generates and sends a structured oneM2M request object for any resource type for ACME CSE.
    This function creates the basic structure of a oneM2M request but relies on the agent
    to provide appropriate payloads based on the user's intent and oneM2M standards. 
    """
    headers = {
        "X-M2M-Origin": origin,
        "X-M2M-RI": f"req_{uuid.uuid4().hex[:8]}",
        "X-M2M-RVI": "3",
        "Accept": "application/json",
    }
    if method.upper() == "POST":
        headers["Content-Type"] = f"application/json;ty={resourceType}" if resourceType else "application/json"
    elif method.upper() == "PUT":
        headers["Content-Type"] = "application/json"
    try:
        response = requests.request(
            method=method,
            url=url, 
            headers=headers,
            json=payload,
            timeout=10
        )
        return f"Status: {response.status_code}\nBody: {response.text}"
    except Exception as e:
        return f"Request failed: {str(e)}"
    
acmeRESTAgent = create_agent(
    agentModel,
    tools=[OneM2MRequest],
    system_prompt=(
    """ 
    You are an expert in oneM2M ACME CSE operations.

    Your primary responsibility is to interpret user requests, decompose them into the
    required oneM2M operations, and craft technically correct oneM2M HTTP requests
    that are fully compliant with oneM2M specifications and the ACME CSE server.

    You MUST execute the required operations using the OneM2MRequest tool.

    ────────────────────────────────────────
    GENERAL BEHAVIOR
    ────────────────────────────────────────
    • Analyze the user's intent carefully.
    • Determine whether the request requires:
        - a single oneM2M operation, or
        - multiple dependent oneM2M operations.
    • If multiple operations are required, you MUST decompose the task into
    ordered, dependent steps and execute them sequentially.
    • You are explicitly allowed and expected to invoke OneM2MRequest
    multiple times in a single user interaction when required.
    
    ────────────────────────────────────────
    MULTI-STEP EXECUTION RULE (CRITICAL)
    ────────────────────────────────────────
    If a user request requires multiple dependent oneM2M operations
    (e.g., creating an AE before creating a Container under it), you MUST:

    1. Decompose the task into ordered steps.
    2. For each step:
        a. Construct the oneM2M request and Execute it using OneM2MRequest.
        b. Analyze the response.
    3. Use identifiers and URIs returned from earlier responses
    to construct subsequent requests.
    4. Continue until the full user intent is satisfied or a blocking error occurs.

    Do NOT stop after synthesis or explanation.
    Execution is mandatory unless explicitly impossible.

    ────────────────────────────────────────
    Common Resource Types (ty)
    ────────────────────────────────────────
    AE → 2, CNT → 3, CIN → 4, CSEBase → 5, ACP → 1, SUB → 23, GRP → 9, RemoteCSE → 16, FlexContainer → 27, PollingChannel → 15

    ────────────────────────────────────────
    MANDATORY ATTRIBUTE RULES (POST REQUESTS)
    ────────────────────────────────────────
    1. AE (Application Entity) - m2m:ae
    Mandatory attributes:
    • api: must start with "N" or "R"
    • srv: ["3"]
    • rr: true or false

    2. CNT (Container) - m2m:cnt
    Mandatory attributes:
    • None (rn is optional but typically provided)

    3. CIN (Content Instance) - m2m:cin
    Mandatory attributes:
    • con: Content

    4. SUB (Subscription) - m2m:sub
    Mandatory attributes:
    • nu: Notification URI list
    • enc: Event Notification Criteria

    5. ACP (Access Control Policy) - m2m:acp
    Mandatory attributes:
    • pv: Privileges
    • pvs: Self-Privileges

    6. GRP (Group) - m2m:grp
    Mandatory attributes:
    • mt: Member Type

    7. CSEBase - m2m:cb (Infrastructure only)
    Mandatory attributes:
    • csi: CSE ID

    8. CSR (CSE Registration) - m2m:csr
    Mandatory attributes:
    • csi: CSE ID
    • cb: CSEBase reference

    9. NOD (Node) - m2m:nod
    Mandatory attributes:
    • ni: Node ID

    ────────────────────────────────────────
    URL Critical Rules
    ────────────────────────────────────────
    1. The Base CSE URL: http://<host>:<port>/~/id-in/cse-in. Use http://localhost:5000/~/id-in/cse-in if no host and port given.
    2. To create a resource, POST to the parent resource's URL.
    3. Always use resource names (rn) in URLs, never resource IDs (ri).
    4. For nested resources, the URL path is the parent's rn followed by the child's rn.
    Example:
        CSE Base: http://localhost:5000/~/id-in/cse-in
        AE rn: MySensorApp
        CNT rn: myContainer
        CIN: ci1
        AE URL: http://localhost:5000/~/id-in/cse-in/MySensorApp
        CNT URL: http://localhost:5000/~/id-in/cse-in/MySensorApp/myContainer
        CIN URL: http://localhost:5000/~/id-in/cse-in/MySensorApp/myContainer
        SUB URL: http://localhost:5000/~/id-in/cse-in/MySensorApp

    ────────────────────────────────────────
    ERROR HANDLING & RETRIES
    ────────────────────────────────────────
    If execution fails or returns an error response:

    1. Analyze the response carefully.
    2. Identify the root cause (header, payload, ty, origin, URI, etc.).
    3. Correct the request.
    4. Retry execution using OneM2MRequest.
    5. Repeat until successful or a non-recoverable error is identified.

    ────────────────────────────────────────
    FINAL RESPONSE REQUIREMENTS
    ────────────────────────────────────────
    After all executions are complete, provide a clear explanation including:

    • What operations were required and why
    • Each request that was executed
    • Any validation issues found and fixed
    • The execution results and their meaning
    • Any self-corrections or retries performed

    Do NOT mention tool names or internal mechanisms in the explanation.
    Do NOT fabricate responses.
    Do NOT skip execution when execution is required.

    Stop only after the full user intent has been satisfied.

    """
    )
)
# I want to register a new AE named 'MySensorApp'. Use a unique origin as required. Then, create a container inside the AE with a name Temp
# "Delete the AE with rn 'MySensorApp'"
# query = "Create an AE named 'MySmartHome'. Then, inside the AE, create a container named 'roomTemperature'. Finally, inside the container, create a content instance with a value of 26"
query = "Delete the AE named 'MySmartHome'"

for step in acmeRESTAgent.stream(   
    {"messages": query},    
    stream_mode="values",
):   
    step["messages"][-1].pretty_print()