import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. PAGE CONFIG & SIDEBAR ---
st.set_page_config(page_title="oneM2M Professor", page_icon="🎓", layout="wide")

with st.sidebar:
    st.title(" Course Materials")
    st.markdown("""
    **Active Specifications:**
    - TS-0001 (Architecture)
    - TS-0004 (Protocols)
    - ACME CSE Documentation
    
    **Current Status:**  Knowledge Base Linked
    """)
    if st.button("Clear Classroom (Reset Chat)"):
        st.session_state.messages = []
        st.rerun()

# --- 2. SESSION STATE (MEMORY) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# --- 3. THE CHAT INTERFACE & STREAMING ---
if prompt := st.chat_input("Ask a question about oneM2M..."):
    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        # We use st.write_stream to handle tokens as they arrive
        # LangGraph's .stream() allows us to see what's happening at each node
        placeholder = st.empty()
        full_response = ""
        
        # Configuration for LangGraph memory
        config = {"configurable": {"thread_id": "classroom_session_1"}}
        
        # We stream the messages from the 'professor' node
        for chunk in professor_agent.stream({"messages": st.session_state.messages}, config, stream_mode="messages"):
            # Check if the chunk is from the assistant's message
            if isinstance(chunk[0], AIMessage):
                full_response += chunk[0].content
                placeholder.markdown(full_response + "▌")
        
        placeholder.markdown(full_response)
        st.session_state.messages.append(AIMessage(content=full_response))