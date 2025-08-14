import streamlit as st
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory.v2 import Memory, SessionSummarizer
from agno.tools.serper import SerperTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.reasoning import ReasoningTools

# Page configuration
st.set_page_config(
    page_title="Research Agent",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("🔬 Research Agent")
st.write("Powered by Agno Framework & GPT-5")

def initialize_agent():
    """Initialize the Agno research agent with memory and tools"""
    
    # Session summarizer for memory
    session_summarizer = SessionSummarizer(
        model=OpenAIChat(id="gpt-5"),
        additional_instructions="""
        Create a concise summary of the research conversation:
        - Key topics researched
        - Important findings and insights
        - Questions asked and answered
        - Research methodology used
        Keep it structured and easy to reference.
        """,
    )
    
    # Memory configuration
    memory = Memory(
        summarizer=session_summarizer,
    )
    
    # Initialize the research agent
    agent = Agent(
        model=OpenAIChat(id="gpt-5-mini"),
        memory=memory,
        tools=[
            SerperTools(),
            WikipediaTools(),
            ReasoningTools()
        ],
        add_history_to_messages=True,
        num_history_runs=3,
        enable_session_summaries=True,
        instructions="""
        You are a fast and efficient research agent with access to web search and Wikipedia.
        
        Your approach:
        - Provide quick, focused responses
        - Use 1-2 sources maximum per query
        - Be concise but informative
        - Focus on the most relevant information
        
        Keep responses:
        - Under 300 words when possible
        - Well-structured with key points
        - Include 1-2 most relevant sources
        - Direct and to the point
        """,
        markdown=True,
        show_tool_calls=False,
    )
    
    return agent

# Sidebar for API key input and details
with st.sidebar:
    # === CONFIGURATION SECTION ===
    st.markdown("### ⚙️ Configuration")
    
    # API Key inputs with better styling
    if 'openai_api_key' not in st.session_state:
        st.session_state.openai_api_key = ''
    if 'serper_api_key' not in st.session_state:
        st.session_state.serper_api_key = ''
    
    st.markdown("**🔑 OpenAI API Key**")
    st.session_state.openai_api_key = st.text_input(
        "Enter your OpenAI API Key",
        type="password",
        value=st.session_state.openai_api_key,
        placeholder="sk-...",
        help="Get your API key from OpenAI"
    )
    
    st.markdown("**🔍 Serper API Key**")
    st.session_state.serper_api_key = st.text_input(
        "Enter your Serper API Key",
        type="password",
        value=st.session_state.serper_api_key,
        placeholder="Your Serper key...",
        help="Get your API key from Serper.dev"
    )
    
    # Connection status
    if st.session_state.openai_api_key:
        os.environ["OPENAI_API_KEY"] = st.session_state.openai_api_key
        st.success("✅ OpenAI API Key configured")
    else:
        st.warning("⚠️ Please enter your OpenAI API key to start")
    
    if st.session_state.serper_api_key:
        os.environ["SERPER_API_KEY"] = st.session_state.serper_api_key
        st.success("✅ Serper API Key configured")
    else:
        st.info("ℹ️ Serper key optional for web search")
    
    st.markdown("---")
    
    # === AGENT INFO SECTION ===
    st.markdown("### 🤖 Agent Information")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Model:**")
        st.markdown("**Memory:**")
        st.markdown("**Tools:**")
    with col2:
        st.markdown("`GPT-5`")
        st.markdown("🟢 Enabled")
        st.markdown("Search, Wiki, Reasoning")
    
    st.markdown("---")
    
    # === ACTIONS SECTION ===
    st.markdown("### 🎯 Actions")
    
    if st.button("🔄 Start New Chat", use_container_width=True, type="primary"):
        st.session_state.messages = []
        st.session_state.agent = None
        st.rerun()
    
    if st.button("🗑️ Clear History", use_container_width=True):
        if 'messages' in st.session_state:
            st.session_state.messages = []
            st.session_state.agent = None
            st.success("Chat history cleared!")
            st.rerun()

# Initialize agent if not exists
if "agent" not in st.session_state and st.session_state.openai_api_key:
    try:
        with st.spinner("🤖 Initializing research agent..."):
            st.session_state.agent = initialize_agent()
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to research?"):
    if not st.session_state.openai_api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
        st.stop()

    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    if "agent" in st.session_state:
        try:
            with st.chat_message("assistant"):
                with st.spinner("🔬 Researching..."):
                    response = st.session_state.agent.run(prompt)
                    st.markdown(response.content)
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.content})

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Agent not initialized. Please check your API keys.")

