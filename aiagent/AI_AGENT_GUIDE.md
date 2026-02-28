# 🤖 Understanding AI Agents - Complete Guide

## What is an AI Agent?

An AI Agent is an autonomous system that can:
- **Perceive** the environment (receive questions/input)
- **Think** about what to do (LLM decides)
- **Act** by using tools (search, calculate, etc.)
- **Learn** from the interaction

### Simple Formula:
```
User Question → LLM (Reasoning) → Choose Tool → Execute Tool → Return Answer
```

---

## Key Components of an AI Agent

### 1. **Large Language Model (LLM)**
The "brain" that decides what to do. In our case: `GPT-4o-mini` via GitHub Models

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
)
```

### 2. **Tools**
Functions the agent can use to solve problems. Examples:
- Web Search
- Calculator
- Database Query
- Email Sender
- Weather API

```python
Tool(
    name="web_search",
    func=search_web,
    description="Search the web for information"
)
```

### 3. **Prompt/System Message**
Instructs the LLM how to behave

```python
system_prompt = "You are a helpful AI assistant that can search the web and do calculations."
```

### 4. **Agent Executor**
Orchestrates the loop: Think → Act → Observe → Repeat

```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)
```

---

## How Your AI Agent Works (Step-by-Step)

### Example: User asks "What's 100 * 50?"

1. **Input**: User question enters the agent
2. **Agent Thinks**: LLM analyzes: "I need to calculate 100 * 50"
3. **Tool Selection**: Agent chooses `calculator` tool
4. **Execution**: `calculator("100 * 50")` runs → returns `5000`
5. **Reasoning**: Agent says "The answer is 5000"
6. **Output**: Final response to user

---

## Setting Up Your GitHub Models Token

### Step 1: Create a Fine-Grained Personal Access Token
1. Go to: https://github.com/settings/tokens?type=beta
2. Click "Generate new token"
3. Give it a name: "AI Agent Token"
4. Under "Repository Access": Select "Public Repositories (read-only)"
5. Under "Permissions": Check "read:packages"
6. Generate and copy the token

### Step 2: Create `.env` File
```bash
cp .env.example .env
# Edit .env and paste your token
GITHUB_TOKEN=ghp_your_token_here
```

### Step 3: Verify Setup
```bash
python my_first_agent.py
```

---

## Tools in Your Agent

### 🔍 Tool 1: Web Search
**Purpose**: Fetch real-time information
**When to use**: Current news, facts, real-time data
**Example**: "What's trending on Twitter?"

```python
def search_web(query: str) -> str:
    """Search the web using DuckDuckGo"""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    return formatted_results
```

### 🧮 Tool 2: Calculator
**Purpose**: Mathematical computations
**When to use**: Calculations, math problems
**Example**: "Calculate 1234 * 5678"

```python
def calculate(expression: str) -> str:
    """Calculate mathematical expressions"""
    result = eval(expression, {"__builtins__": {}}, {})
    return f"Result: {result}"
```

---

## Adding New Tools to Your Agent

### Example: Add a Weather Tool

```python
def get_weather(location: str) -> str:
    """Get weather for a location"""
    # You'd integrate with a weather API like OpenWeatherMap
    return f"Weather in {location}: Sunny, 25°C"

weather_tool = Tool(
    name="weather",
    func=get_weather,
    description="Get current weather for any location"
)

tools = [web_search_tool, calculator_tool, weather_tool]
```

---

## Common Patterns

### Pattern 1: Research Question
```
Question: "Who invented the telephone?"
Agent: I need current information → Use web_search → Returns answer
```

### Pattern 2: Math Problem
```
Question: "What's 15% of 5000?"
Agent: This is math → Use calculator → Returns 750
```

### Pattern 3: Complex Question
```
Question: "What's the average height of NBA players times 2?"
Agent: Needs web search (for stats) + calculator (for math) → Chains both
```

---

## Understanding the Agent Loop

```
┌─────────────────────────────────────┐
│  User asks a question               │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  LLM analyzes: "What do I need?"    │
└──────────────┬──────────────────────┘
               ↓
         ┌─────────────┐
         │ Need tools? │
         └─────┬──────┘
        YES ↙       ↖ NO
         ↓           ↓
    ┌────────────┐  ┌──────────────────┐
    │ Use tools  │  │ Return direct     │
    │ Search/    │  │ answer from LLM   │
    │ Calculate  │  └──────────────────┘
    └────┬───────┘
         ↓
    ┌────────────────────┐
    │ Combine tool output│
    │ with reasoning     │
    └────┬───────────────┘
         ↓
    ┌────────────────────┐
    │ Final answer to    │
    │ user               │
    └────────────────────┘
```

---

## Why Use AI Agents?

✅ **Automation**: Handle complex tasks automatically
✅ **Accuracy**: Use real tools instead of hallucinating
✅ **Flexibility**: Add new tools as needed
✅ **Intelligence**: Reason about which tool to use
✅ **Real-time**: Get current information via web search
✅ **Scalability**: Same agent can handle many different types of questions

---

## Best Practices

1. **Tool Descriptions Matter**: Clear descriptions help the LLM choose the right tool
   ```python
   # Good ✅
   "Search the web for current information about {query}"
   
   # Bad ❌
   "Web search"
   ```

2. **Error Handling**: Always handle exceptions
   ```python
   try:
       result = web_search(query)
   except Exception as e:
       return f"Error: {str(e)}"
   ```

3. **Safety**: Don't allow arbitrary code execution
   ```python
   # Safe ✅
   eval(expression, {"__builtins__": {}}, {})
   
   # Dangerous ❌
   eval(expression)
   ```

4. **Testing**: Test each tool independently first
   ```python
   print(calculate("10 + 5"))  # Test directly
   ```

---

## Limitations & Future Improvements

### Current Limitations:
- ❌ Can't access private information (files, databases)
- ❌ No memory between conversations
- ❌ Limited to synchronous operations
- ❌ No image processing

### Improvements You Can Add:
- 📝 Add conversation memory (save previous interactions)
- 📊 Add PDF/file reading tool
- 🖼️ Add image analysis capability
- 💾 Add database query tool
- 🔗 Chain agents together for complex tasks
- 🌐 Add API integration tools

---

## Running Your Agent

### Basic Usage:
```bash
python my_first_agent.py
```

### Interactive Mode:
Modify the script to accept user input:
```python
while True:
    question = input("\n❓ Ask me something: ")
    if question.lower() == "exit":
        break
    answer = ask_agent(question)
    print(f"\n✅ Answer: {answer}\n")
```

---

## Next Steps

1. ✅ Setup GitHub token
2. ✅ Install dependencies: `pip install langchain openai duckduckgo-search python-dotenv`
3. ✅ Create `.env` with your token
4. ✅ Run the agent: `python my_first_agent.py`
5. ✅ Add more tools as needed
6. ✅ Build a web interface (Flask/FastAPI)
7. ✅ Deploy to production

---

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [GitHub Models](https://github.com/marketplace/models)
- [OpenAI API](https://platform.openai.com/docs)
- [DuckDuckGo API](https://duckduckgo.com/api)

---

Happy building! 🚀
