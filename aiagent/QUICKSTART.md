# 🚀 Quick Start Guide - AI Agent Setup

## 📋 Prerequisites
- Python 3.8+
- GitHub account with a personal access token
- Terminal/Command prompt

---

## 🔧 Setup in 5 Steps

### Step 1: Create GitHub Token
1. Visit: https://github.com/settings/tokens?type=beta
2. Click "Generate new token"
3. Name: "AI Agent"
4. Select "Public Repositories (read-only)"
5. Check "read:packages" permission
6. Copy the token (starts with `ghp_`)

### Step 2: Setup Environment
```bash
cd /Users/vishalkumarbg/Documents/AI_ML_DOCS/aiml
bash setup.sh
```

### Step 3: Configure Token
Edit `.env` file:
```bash
nano .env
```

Replace `your_github_token_here` with your actual token:
```
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Save and exit (Ctrl+O, Enter, Ctrl+X)

### Step 4: Verify Installation
```bash
python3 -c "import langchain; print('✅ LangChain installed')"
```

### Step 5: Run Your Agent
```bash
# Option A: Batch mode with predefined questions
python3 my_first_agent.py

# Option B: Interactive mode (recommended for learning)
python3 interactive_agent.py
```

---

## 📚 File Guide

| File | Purpose |
|------|---------|
| `my_first_agent.py` | Original batch agent with test questions |
| `interactive_agent.py` | Interactive chat interface (👈 Start here!) |
| `AI_AGENT_GUIDE.md` | Complete explanation of AI agents |
| `requirements.txt` | Python package dependencies |
| `.env` | Your GitHub token (CREATE THIS!) |
| `setup.sh` | Automated setup script |

---

## 🎯 Understanding the Flow

```
                 ┌─────────────────────┐
                 │   User Question     │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │  LLM (GPT-4o-mini)  │
                 │ Processes question  │
                 └──────────┬──────────┘
                            ↓
                   ┌────────────────────┐
                   │ Needs tools?       │
                   └────────┬───────────┘
                       ╱    │    ╲
                     YES   MAYBE   NO
                     ↙      ↓      ↘
                ┌────┐  ┌────┐  ┌─────────┐
                │Web │  │Calc│  │Direct   │
                │Src │  │    │  │Answer   │
                └──┬─┘  └──┬─┘  └────┬────┘
                   │       │         │
                   └───┬───┴────┬────┘
                       ↓
              ┌──────────────────────┐
              │ Combine results with │
              │ reasoning            │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │ Final Answer to User │
              └──────────────────────┘
```

---

## 💡 Key Concepts

### What is an Agent?
An AI Agent is like a smart assistant that can:
- **Listen**: Understand your question
- **Think**: Decide what to do
- **Act**: Use tools (search, calculate, etc.)
- **Answer**: Give you accurate results

### What are Tools?
Functions the agent can call:
- `web_search`: Find information online
- `calculator`: Do math
- `time`: Get current time
- (You can add more!)

### How Does It Decide?
The LLM reads your question and decides:
- "Do I need web search?" ✓
- "Do I need calculator?" ✓
- "Can I answer directly?" ✓

---

## 🧪 Example Interactions

### Example 1: Simple Question
```
You: "What is 100 * 50?"
Agent: Uses calculator tool → "Result: 5000"
```

### Example 2: Research Question
```
You: "What's the current Bitcoin price?"
Agent: Uses web_search tool → Finds current price → "Bitcoin is currently..."
```

### Example 3: Complex Question
```
You: "What's 20% more than yesterday's Bitcoin price?"
Agent: Uses web_search (find price) + calculator (do math) → Gives answer
```

---

## ✅ Troubleshooting

### Error: "GITHUB_TOKEN not found"
**Solution**: 
```bash
cat .env
# Make sure it shows your token, not "your_github_token_here"
```

### Error: "Import langchain failed"
**Solution**: 
```bash
pip install -r requirements.txt
```

### Error: "DuckDuckGo search failed"
**Reason**: Internet might be down or DuckDuckGo is temporarily unavailable
**Solution**: Try again in a moment

### Agent takes too long
**Reason**: First run might be slow as it downloads models
**Solution**: Be patient, subsequent runs are faster

---

## 🎨 Try These Questions!

1. **Math**: "Calculate 1234 * 5678"
2. **Search**: "What's trending in AI?"
3. **Time**: "What time is it?"
4. **Complex**: "Calculate 50% of 1000, then double it"
5. **Current**: "Who won the latest World Cup?"
6. **Complex**: "Search for Python tips, then count how many you found"

---

## 🚀 Next Steps

### Level 1: Basic Understanding
- ✅ Run the interactive agent
- ✅ Ask different types of questions
- ✅ Read the verbose output to understand thinking

### Level 2: Customization
- ✅ Add more tools (weather, news, etc.)
- ✅ Change the system prompt
- ✅ Modify test questions

### Level 3: Advanced
- ✅ Save conversation history
- ✅ Add database tool
- ✅ Create a web interface (Flask/FastAPI)
- ✅ Deploy to cloud (Heroku/AWS)

---

## 📖 Learning Resources

- [LangChain Docs](https://python.langchain.com/)
- [GitHub Models](https://github.com/marketplace/models)
- [OpenAI API](https://platform.openai.com/docs)
- [AI Agent Concepts](https://en.wikipedia.org/wiki/Agent_architecture)

---

## 🤝 Getting Help

1. Check verbose output (it shows the agent's thinking)
2. Try a simpler question first
3. Read `AI_AGENT_GUIDE.md` for detailed explanations
4. Check `.env` file has your token

---

## 🎉 You're Ready!

Run this to start:
```bash
python3 interactive_agent.py
```

Happy building! 🚀
