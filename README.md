# 🔬 Agno Research Agent - Streamlit App

A fast and efficient research agent built with **Agno framework**, **GPT-5**, and **Streamlit** that provides intelligent research capabilities with memory and reasoning.

## ✨ Features

- **🤖 GPT-5 Powered**: Uses OpenAI's latest model for intelligent responses
- **🧠 Memory System**: Remembers conversation context and builds session summaries
- **🔍 Multi-Source Research**: 
  - Serper web search and news
  - Wikipedia knowledge base access
  - Advanced reasoning capabilities
- **💬 Clean Chat Interface**: Qwen-style minimal UI with native Streamlit chat
- **⚡ Fast Performance**: Optimized for quick, focused responses
- **🎯 Efficient Research**: Direct answers with 1-2 sources maximum

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or navigate to the project directory
cd agno_research_agent

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Setup

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🛠️ Configuration

### API Keys Required

- **OpenAI API Key**: Required for GPT-5 model access
  - Get yours at: https://platform.openai.com/account/api-keys
  - Enter directly in the sidebar (secure password input)

- **Serper API Key**: Required for web search functionality
  - Get free key at: https://serper.dev
  - Enter directly in the sidebar (optional but recommended)

## 💡 Usage Examples

### Research Queries
- "Research the latest developments in quantum computing"
- "Compare renewable energy technologies and their efficiency"
- "What are the current trends in artificial intelligence safety?"
- "Explain the economic impact of remote work post-pandemic"

### Follow-up Questions
- "Can you elaborate on the quantum supremacy achievements?"
- "What are the challenges facing solar energy adoption?"
- "How do these AI safety measures compare to previous approaches?"

## 🏗️ Architecture

### Core Components

1. **Agno Agent**: Main research agent with GPT-4o
2. **Memory System**: Session summarization and context retention
3. **Tool Integration**: 
   - DuckDuckGo search tools
   - Wikipedia access tools
   - Reasoning tools
4. **Streamlit Interface**: Interactive web application

### Agent Configuration

```python
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
)
```

## 📋 Dependencies

- **agno**: Core agent framework
- **streamlit**: Web application framework
- **openai**: GPT-5 model access
- **wikipedia**: Wikipedia API access
- **requests**: HTTP requests
- **beautifulsoup4**: Web scraping support
- **rich**: Enhanced terminal output

## 🎯 Key Features Explained

### Memory System
- **Session Summaries**: Automatically summarizes conversation topics and insights
- **Context Retention**: Remembers previous questions and builds upon them
- **Structured Memory**: Organized storage of research findings

### Research Methodology
1. **Question Analysis**: Breaks down complex queries
2. **Multi-Source Search**: Uses web search and Wikipedia
3. **Information Synthesis**: Combines and analyzes findings
4. **Structured Response**: Presents information clearly with citations

### User Interface
- **Qwen-Style Chat**: Native Streamlit chat messages for clean UX
- **Sidebar Configuration**: Clean API key management with status indicators
- **Agent Information**: Model, memory, and tools status display
- **Session Controls**: Start new chat and clear history buttons
- **Real-time Feedback**: Research progress with spinner indicators

## 🔧 Customization

### Modify Agent Instructions
Edit the `instructions` parameter in the `initialize_agent()` function to customize the agent's behavior.

### Add New Tools
Extend the `tools` list with additional Agno tools:
- Financial tools (YFinance)
- Email tools
- File system tools
- Custom tools

### Performance Tuning
- Adjust `num_history_runs` for memory vs speed trade-off
- Toggle `enable_session_summaries` for faster responses
- Modify agent instructions for response length control

### UI Customization
Modify the CSS in the `st.markdown()` sections to change the appearance.

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your OpenAI API key is valid and has sufficient credits
2. **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
3. **Memory Issues**: Clear session history if the app becomes slow

### Debug Mode
Set `show_tool_calls=True` in the agent configuration to see detailed tool usage.

### Performance Issues
- Reduce `num_history_runs` for faster responses
- Disable session summaries if not needed
- Check API key quotas and rate limits

## 📈 Performance

- **Agent Instantiation**: ~3μs (Agno framework optimization)
- **Memory Usage**: ~6.5KB per agent instance
- **Response Time**: 10-20 seconds (optimized for speed)
- **Memory Context**: 3 conversation turns (balanced performance)
- **Research Scope**: 1-2 sources maximum for faster results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Links

- [Agno Documentation](https://docs.agno.com)
- [Agno GitHub](https://github.com/agno-agi/agno)
- [OpenAI API](https://platform.openai.com)
- [Streamlit Documentation](https://docs.streamlit.io)

---

**Built with ❤️ using Agno, GPT-5, and Streamlit**
