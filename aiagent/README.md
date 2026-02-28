# 🤖 My First AI Agent - Complete Learning Project

A hands-on project to understand how AI agents work using GitHub Models (free) and LangChain.

## 📚 What You'll Learn

- ✅ How AI agents think and make decisions
- ✅ How to connect to GitHub's free AI models
- ✅ How to create and use tools
- ✅ How to build an interactive assistant
- ✅ How to chain multiple tools together
- ✅ How to handle errors gracefully

## 🎯 Quick Start (5 Minutes)

### 1. Get GitHub Token
Visit: https://github.com/settings/tokens?type=beta
- Create new token with `read:packages` scope
- Copy the token (starts with `ghp_`)

### 2. Setup Project
```bash
cd /Users/vishalkumarbg/Documents/AI_ML_DOCS/aiml
bash setup.sh
```

### 3. Add Token
Edit `.env`:
```bash
nano .env
```
Add your token:
```
GITHUB_TOKEN=ghp_your_token_here
```

### 4. Run Agent
```bash
python3 interactive_agent.py
```

### 5. Ask Questions!
```
👤 You: Calculate 1234 * 5678
🤖 Agent: Result: 7006652

👤 You: What's trending in AI?
🤖 Agent: (searches web and provides current info)

👤 You: exit
👋 Goodbye!
```

## 📁 Project Files

```
my_first_agent.py          # Batch mode agent (predefined questions)
interactive_agent.py       # Interactive chat agent (👈 Start here!)
requirements.txt           # Python dependencies
.env                       # Your GitHub token (CREATE THIS!)
.env.example               # Template for .env

DOCUMENTATION:
README.md                  # This file
QUICKSTART.md              # Quick setup guide
CONCEPTS.md                # Deep dive into AI agents
AI_AGENT_GUIDE.md          # Comprehensive guide
setup.sh                   # Automated setup script
```

## 🧠 How It Works

### Simple Model
```
Question → LLM Thinks → Selects Tools → Executes → Answers
```

### Complex Model
```
             ┌─────────────────┐
             │  User Question  │
             └────────┬────────┘
                      ↓
           ┌──────────────────────┐
           │ LLM Analyzes         │
           │ "What tools needed?" │
           └────────┬─────────────┘
                    ↓
           ┌────────────────────┐
         YES    Tool Needed?    NO
           │                    │
           ↓                    ↓
    ┌────────────┐      ┌──────────────┐
    │ Execute    │      │ Answer from  │
    │ Tool(s)    │      │ LLM          │
    └────┬───────┘      └──────────────┘
         ↓
    ┌────────────────────────┐
    │ Combine & Reason       │
    │ Final Answer           │
    └────────────────────────┘
```

## 🛠️ Available Tools

| Tool | Purpose | Example |
|------|---------|---------|
| `web_search` | Search the web | "What's trending?" |
| `calculator` | Do math | "100 * 50" |
| `time` | Get current time | "What time is it?" |

## 📖 Learning Path

### Beginner (30 minutes)
- [ ] Read QUICKSTART.md
- [ ] Run `python3 interactive_agent.py`
- [ ] Ask different types of questions
- [ ] Observe verbose output

### Intermediate (1 hour)
- [ ] Read CONCEPTS.md
- [ ] Understand the agent loop
- [ ] Modify the system prompt
- [ ] Change test questions

### Advanced (2+ hours)
- [ ] Read AI_AGENT_GUIDE.md
- [ ] Add new tools (weather, database, etc.)
- [ ] Create interactive features
- [ ] Handle edge cases
- [ ] Add conversation memory

## 🔧 Adding Your Own Tools

### Example: Add a Temperature Converter

```python
def convert_temperature(celsius: float) -> str:
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C = {fahrenheit}°F"

# Add to tools
temp_tool = Tool(
    name="temp_converter",
    func=convert_temperature,
    description="Convert temperature from Celsius to Fahrenheit"
)

tools = [web_search_tool, calculator_tool, temp_tool]
```

### Example: Add a Random Fact Tool

```python
def get_random_fact() -> str:
    """Get a random interesting fact"""
    import requests
    try:
        response = requests.get("https://api.api-ninjas.com/v1/facts")
        data = response.json()
        return data[0]['fact']
    except:
        return "Could not fetch fact"

# Add to tools
fact_tool = Tool(
    name="random_fact",
    func=get_random_fact,
    description="Get a random interesting fact"
)
```

## 🎯 Example Conversations

### Math Example
```
You: "Calculate 50% of 2000"
Agent: (Uses calculator) "Result: 1000"
```

### Research Example
```
You: "Who is the current CEO of OpenAI?"
Agent: (Uses web_search) "Sam Altman is the current CEO of OpenAI"
```

### Complex Example
```
You: "If Bitcoin is at $100k and I have $5k, how much Bitcoin can I buy?"
Agent: (Uses web_search for price, calculator for math)
       "At current price, you can buy approximately 0.05 BTC"
```

## ⚙️ Customization

### Change Agent Behavior
Edit the system prompt in `interactive_agent.py`:
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Your custom instructions here"),
    ...
])
```

### Change Temperature (Creativity)
```python
llm = ChatOpenAI(
    temperature=0.3  # Lower = more focused, higher = more creative
)
```

### Add/Remove Tools
```python
tools = [
    web_search_tool,
    calculator_tool,
    time_tool,
    # Add your tools here
]
```

## 🐛 Troubleshooting

### Issue: "GITHUB_TOKEN not found"
**Solution**: Check `.env` file exists and has your token
```bash
cat .env
```

### Issue: "Import langchain failed"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "Web search not working"
**Solution**: Check internet connection, try again
```bash
python3 -c "from duckduckgo_search import DDGS; print('✅ DuckDuckGo working')"
```

### Issue: "Agent is too slow"
**Solution**: First run downloads models. Subsequent runs are faster.

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [AI Agent Research Paper](https://arxiv.org/abs/2402.00696)

## 🚀 Next Steps

### Level 1: Master the Basics
- Use the interactive agent daily
- Try different question types
- Understand the verbose output

### Level 2: Experiment
- Modify prompts
- Add new tools
- Change temperature/model settings

### Level 3: Deploy
- Create a web interface (Flask/FastAPI)
- Add conversation history
- Deploy to cloud (Heroku/AWS)
- Add database integration

### Level 4: Advanced
- Use multiple agents in combination
- Implement memory systems
- Add real-time data sources
- Create domain-specific agents

## 💡 Key Concepts Summary

| Concept | Explanation |
|---------|------------|
| **Agent** | AI system that can reason and use tools |
| **LLM** | Large Language Model (the "brain") |
| **Tool** | Function agent can call to solve problems |
| **Prompt** | Instructions for how agent should behave |
| **Token** | Authentication for GitHub Models |
| **Verbose** | Show agent's thinking process |
| **Tool Calling** | When agent decides to use a tool |
| **Chaining** | Using multiple tools in sequence |

## 🎓 What Makes A Good Agent?

✅ **Clear Tool Descriptions**: Agent knows when to use each tool
✅ **Error Handling**: Gracefully handles failures
✅ **Safety**: Prevents unauthorized operations
✅ **Efficiency**: Uses minimal API calls
✅ **Transparency**: Shows reasoning (verbose mode)
✅ **Reliability**: Consistent results

## 📝 Example Prompts to Try

1. "What is the capital of India?"
2. "Calculate 999 * 888"
3. "Tell me about Python programming"
4. "What's 25% of 400?"
5. "What time is it right now?"
6. "Search for the latest AI news"
7. "Calculate the average of 10, 20, and 30"
8. "Who invented the internet?"

## 🤝 Contributing

Found a bug or want to improve this project? 
- Test the agents
- Try different prompts
- Suggest new tools
- Improve documentation

## 📄 License

This project is for learning purposes. Use freely!

## 🎉 Ready to Start?

```bash
cd /Users/vishalkumarbg/Documents/AI_ML_DOCS/aiml
python3 interactive_agent.py
```

Ask your first question! 🚀

---

**Happy Learning!** 
For questions, refer to the documentation files or try simpler prompts first.
