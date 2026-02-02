import os
# LangSmith Tracing
from dotenv import load_dotenv
load_dotenv() 
tracingEnabled = os.getenv("LANGSMITH_TRACING")
# Python Typing
from typing import Annotated, Literal
from typing_extensions import TypedDict
import operator
# LangChain & LangGraph
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send
# Pydantic
from pydantic import BaseModel, Field
# Agents
from initializeAgents import oneM2MStandardsAgent, acmeDocsAgent, acmeCodeAgent

# Initialize LLM Model
llmModel = ChatOllama(model="llama3.1:latest", temperature=0)

""" 
routerState Schema
1. userQuery state: user input (e.g., userQuery = "Create an AE") 
2. classifications state: list of queryClassification 
    (e.g., classifcations = [
        { "knowledgeBase": "oneM2MStandards", "llmQuery": "Container" },
        { "knowledgeBase": "oneM2MACMEDocs", "llmQuery": "Setup Docker in ACME" }
    ])
3. results state: list of merged agent outputs (used for parallel processing through operator.add)
(e.g., results = [
    { "knowledgeBaseSource": "oneM2MStandards", "result": "A container is a ..." },
    { "knowledgeBaseSource": "oneM2MStandards", "result": "To setup a docker in ACME ...." },
])
Note: without operator.add, (consider multiple subagents assigning values to results state), 
the results state gets overwritten by the latest value assignment. In contrast, the classifications state, one only node assigns 
value/s to classifications which can be one or more queryClassification.
4. compiledSynthesis state: final compiled output answer (e.g., compiledSynthesis = "To create an AE ...") 
"""

class agentInput(TypedDict):
    agentInputQuery: str

class agentOutput(TypedDict):
    knowledgeBaseSource: str
    result: str

class queryClassification(TypedDict):
    knowledgeBase: Literal["oneM2MStandards", "oneM2MACMEDocs", "oneM2MACMECodebase"]
    llmQuery: str

class classifyQueryResult(BaseModel):
    classifiedQuery: list[queryClassification] = Field(description="List of agents to invoke with their targeted sub-questions")

class routerState(TypedDict):  
    userQuery: str  
    classifications: list[queryClassification] 
    results: Annotated[list[agentOutput], operator.add]
    compiledSynthesis: str

def classifyQuery(state: routerState) -> dict[str, list[queryClassification]]:
    structuredResponse = llmModel.with_structured_output(classifyQueryResult)
    systemContent = """ Analyze the query and determine which knowledge bases to consult.
    For each chosen knowledge source, generate a targeted sub-question or query optimized for that source.
    Knowledge Bases:
    1. oneM2MStandards: oneM2M technical specifications and technical reports
    2. oneM2MACMEDocs: ACME CSE configurations, setup & running, instructions, operation
    3. oneM2MACMECodebase: a python codebase of ACME CSE implementation 
    Return ONLY the sources that are relevant to the query. Each source should have
    a targeted sub-question or query optimized for that specific knowledge domain.
    Example for "What is an AE? How do you register one in ACME?:
    - oneM2MStandards: "What is an AE?"
    - oneM2MACMEDocs: "is AE supported?"
    - oneM2MACMECodebase: "register AE"
    Note: oneM2MACMECodebase is the actual implementation of the ACME CSE. 
    While it does not contain 'how-to' guides, it contains the class definitions 
    and logic flow to infer the correct implementation patterns for user queries.
    """
    response = structuredResponse.invoke([
        {"role": "system", "content": systemContent},
        {"role": "user", "content": state["userQuery"]}
    ])
    """ Input used from routerState: state["userQuery"]
        example input: state["userQuery"] = "What is an AE? How to create one?"
        example output: {"classifications": [   {"knowledgeBase": "oneM2MStandards", "llmQuery": "What is an AE?"}, 
                                                {"knowledgeBase": "oneM2MACMECodebase", "llmQuery": "create AE"}    ]   
    """
    return {"classifications": response.classifiedQuery}

def routeClassifiedToAgents(state: routerState) -> list[Send]:
    """ Input used from routerState: state["classifications"]
        example input: state["classifications"] = [ {"knowledgeBase": "oneM2MStandards", "llmQuery": "What is an AE?"}, 
                                                    {"knowledgeBase": "oneM2MACMECodebase", "llmQuery": "create AE"} ]
        example output: [   Send("oneM2MStandards", {"agentInputQuery": "What is an AE?"}), 
                        Send("oneM2MACMECodebase", {"agentInputQuery": "create AE"})    ]
    """
    return [Send(classified["knowledgeBase"], {"agentInputQuery": classified["llmQuery"]}) for classified in state["classifications"]]

def queryStandards(state: agentInput) -> dict[str, list[agentOutput]]:
    agentResponse = oneM2MStandardsAgent.invoke({"messages": [{"role": "user", "content": state["agentInputQuery"] }]})
    """ Input used from agentInput: state["agentInputQuery"] 
        example input: state["agentInputQuery"] = "What is an AE?"
        example output: {"results": [{"knowledgeBaseSource": "oneM2MStandards", "result": "an AE is a ..."]}
        Note: operator.add will merge the other values of "results" from other agents through parallel fan-out
    """
    return {"results": [{"knowledgeBaseSource": "oneM2M standards (TS and TR)", "result": agentResponse["messages"][-1].content}]}

def queryDocs(state: agentInput) -> dict[str, list[agentOutput]]:
    agentResponse = acmeDocsAgent.invoke({"messages": [{"role": "user", "content": state["agentInputQuery"] }]})
    return {"results": [{"knowledgeBaseSource": "oneM2M CSE ACME Documentation", "result": agentResponse["messages"][-1].content}]}

def queryCodebase(state: agentInput) -> dict[str, list[agentOutput]]:
    agentResponse = acmeCodeAgent.invoke({"messages": [{"role": "user", "content": state["agentInputQuery"] }]})
    return {"results": [{"knowledgeBaseSource": "oneM2M CSE ACME Codebase", "result": agentResponse["messages"][-1].content}]}

def synthesizeResult(state: routerState) -> dict[str, str]:
    if not state.get("results"):
        return {"compiledSynthesis": "No information gathered from agents."}
    knowledgeBaseResult = "\n\n".join([f"Source: {values['knowledgeBaseSource']}\n{values['result']}" for values in state["results"]])
    prompt = f"""
    You are a technical expert specializing in oneM2M standards and the ACME CSE implementation. 
    Your goal is to provide a unified, accurate answer to the user query based ONLY on the provided research findings.
    ### Research Findings:
    {knowledgeBaseResult}
    ### Instructions:
    1. **Cite Your Sources**: When using information, refer to the source name provided (e.g., "According to the one M2M standards...").
    2. **Reconcile Information**: If the Standards (TS/TR) define a concept and the Codebase or Docs explain how it is implemented in ACME, combine these into a single explanation.
    3. **Address Gaps**: If a specific part of the user query was not covered in the findings, explicitly state that the information was not available in the consulted knowledge bases.
    4. **Be Technical and Precise**: Use the correct oneM2M terminology as found in the research results.
    5. **No Hallucinations**: Do not use outside knowledge. Rely strictly on the "Source" blocks provided above.
    Final Answer Format:
    - A concise summary.
    - Detailed technical explanation with citations.
    - (Optional) Implementation notes if ACME-specific data was found.
    """
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": state["userQuery"]}
    ]
    response = llmModel.invoke(messages)
    return {"compiledSynthesis": response.content}


learnOneM2MWorkflow = StateGraph(routerState)
learnOneM2MWorkflow.add_node("classifyNode", classifyQuery)
learnOneM2MWorkflow.add_node("oneM2MStandards", queryStandards)
learnOneM2MWorkflow.add_node("oneM2MACMEDocs", queryDocs)
learnOneM2MWorkflow.add_node("oneM2MACMECodebase", queryCodebase)
learnOneM2MWorkflow.add_node("synthesize", synthesizeResult)

learnOneM2MWorkflow.add_edge(START, "classifyNode")
learnOneM2MWorkflow.add_conditional_edges(
    "classifyNode", 
    routeClassifiedToAgents, 
    ["oneM2MStandards", "oneM2MACMEDocs", "oneM2MACMECodebase"]
)

learnOneM2MWorkflow.add_edge("oneM2MStandards", "synthesize")
learnOneM2MWorkflow.add_edge("oneM2MACMEDocs", "synthesize")
learnOneM2MWorkflow.add_edge("oneM2MACMECodebase", "synthesize")
learnOneM2MWorkflow.add_edge("synthesize", END)

app = learnOneM2MWorkflow.compile()

if __name__ == "__main__":
    userInput = "What is an AE and how do I register one in the ACME CSE implementation?"
    initialState = {"userQuery": userInput}

    finalState = app.invoke(initialState)

    print("\n--- Final Synthesis Output ---")
    print(finalState.get("compiledSynthesis"))