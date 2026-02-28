# 🎓 AI Agent Concepts Explained

## Table of Contents
1. [What is an AI Agent?](#what-is-an-ai-agent)
2. [Core Components](#core-components)
3. [How Agents Think](#how-agents-think)
4. [Tools & Functions](#tools--functions)
5. [Decision Making](#decision-making)
6. [Practical Example](#practical-example)
7. [Common Patterns](#common-patterns)
8. [Building Your Own](#building-your-own)

---

## What is an AI Agent?

### Simple Definition
An **AI Agent** is a software program that can:
1. **Perceive** - Understand what the user is asking
2. **Reason** - Decide what to do
3. **Act** - Use tools to accomplish tasks
4. **Communicate** - Return answers to the user

### In Your Case
Your AI agent uses:
- **Brain**: GPT-4o-mini (the LLM)
- **Hands**: Tools like web_search and calculator
- **Ears**: Your questions in the chat
- **Mouth**: Responses back to you

### Why Are They Useful?
```
❌ Regular LLM: "I think Bitcoin is around $50,000" (might be wrong/outdated)
✅ Agent with Tools: Uses web_search → "Bitcoin is currently $98,750"
```

---

## Core Components

### 1. The LLM (Language Model)
**What it does**: Understands language and makes decisions

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",  # The AI model
    api_key=os.getenv("GITHUB_TOKEN"),  # Authentication
    base_url="https://models.inference.ai.azure.com",  # Server
    temperature=0.7  # Creativity level (0-1)
)
```

**Temperature Explained**:
- `0.0` = Deterministic (always same answer)
- `0.5` = Balanced
- `1.0` = Creative (varied answers)

### 2. Tools
**What they are**: Functions the agent can call

```python
Tool(
    name="web_search",  # How agent calls it
    func=search_web,    # Actual function
    description="Search the web..."  # Why to use it
)
```

**Your Tools**:
- `web_search` - Find information online
- `calculator` - Do math safely
- `time` - Get current time

### 3. Prompt
**What it is**: Instructions for the agent

```python
system_prompt = """You are a helpful AI assistant.
- Be conversational
- Use tools when needed
- Provide sources"""
```

### 4. Agent Executor
**What it does**: Runs the agent loop

```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # Show thinking
    max_iterations=10  # Max steps
)
```

---

## How Agents Think

### The Agent Loop (Step-by-Step)

```
STEP 1: INPUT
┌─────────────────────────────────┐
│ User: "What's 100 * 50?"        │
└─────────────┬───────────────────┘
              ↓

STEP 2: LLM ANALYZES
┌─────────────────────────────────┐
│ "This is a math question"       │
│ "I should use calculator tool"  │
└─────────────┬───────────────────┘
              ↓

STEP 3: TOOL SELECTION
┌─────────────────────────────────┐
│ Selected Tool: calculator       │
│ Input: "100 * 50"              │
└─────────────┬───────────────────┘
              ↓

STEP 4: EXECUTION
┌─────────────────────────────────┐
│ calculator("100 * 50")         │
│ Output: "Result: 5000"         │
└─────────────┬───────────────────┘
              ↓

STEP 5: REASONING
┌─────────────────────────────────┐
│ LLM sees: "Result: 5000"       │
│ Thinks: "I have the answer"    │
│ Decision: No more tools needed  │
└─────────────┬───────────────────┘
              ↓

STEP 6: OUTPUT
┌─────────────────────────────────┐
│ "The answer is 5000"            │
└─────────────────────────────────┘
```

### When Does It Use Tools?

**LLM Decision Tree**:
```
                Question
                   │
         ┌─────────┴─────────┐
         ↓                   ↓
    Can I answer      Do I need current
    from training?    information?
      │    │              │
     YES  NO             YES
      │    │              │
      ↓    ↓              ↓
    Answer Need Tool   web_search
```

### How Many Tools Can It Use?

**One Tool** (Most Common):
```
Question: "What is the capital of France?"
Agent: Uses web_search → Returns "Paris"
```

**Multiple Tools** (Chaining):
```
Question: "What's 20% of Bitcoin's current price?"
Agent: 
  1. web_search("bitcoin price") → $98,750
  2. calculator("98750 * 0.2") → 19,750
  Return: "20% of current Bitcoin price is $19,750"
```

---

## Tools & Functions

### Anatomy of a Tool

```python
Tool(
    name="calculator",           # ← What you call it
    func=calculate,              # ← The function it runs
    description="Calculate math" # ← Why the agent uses it
)
```

### Example Tool 1: Web Search

```python
def search_web(query: str) -> str:
    """Search the web"""
    # 1. Take user's search query
    # 2. Use DuckDuckGo API to search
    # 3. Format results nicely
    # 4. Return formatted text
    return formatted_results
```

**When Agent Uses It**:
- "What's trending?"
- "Tell me about Python"
- "Who won the football match?"

### Example Tool 2: Calculator

```python
def calculate(expression: str) -> str:
    """Calculate math safely"""
    # 1. Take math expression like "100 + 50"
    # 2. Evaluate it (safely, no code execution)
    # 3. Return result
    return f"Result: {result}"
```

**When Agent Uses It**:
- "Calculate 100 * 50"
- "What's 25% of 1000?"
- "Add 123 and 456"

### Safety First! ⚠️

**UNSAFE** ❌:
```python
eval(expression)  # Could run ANY code!
```

**SAFE** ✅:
```python
eval(expression, {"__builtins__": {}}, {})  # Only math allowed
```

---

## Decision Making

### How Does the Agent Know Which Tool to Use?

The LLM reads:
1. **Tool Name** - "web_search" suggests searching
2. **Tool Description** - "Search the web for current information"
3. **User Question** - "What's Bitcoin's price?"

### The Matching Process

```
Question: "What's Bitcoin's price?"
          ↓
    Is this math? NO
          ↓
    Do I need current info? YES
          ↓
    Which tool has "current information"? web_search
          ↓
    Use web_search tool
```

### Multiple Interpretations

```
Question: "How many apples cost $50 if each costs $2?"

Interpretation 1 (Math):
  → calculator("50 / 2") = 25 apples ✓

Interpretation 2 (Search):
  → web_search("apple price") = Not helpful

Agent chooses: calculator ✓
```

---

## Practical Example

### Real-World Example: Compound Question

**User Asks**: "If Bitcoin is $100k and I have $5k, how many Bitcoin can I buy?"

### Agent's Thinking:

```
Step 1: Analyze Question
  - Need current Bitcoin price (search)
  - Need to calculate amount (math)

Step 2: Use web_search
  - Input: "Bitcoin price"
  - Output: "Bitcoin is currently $98,750"

Step 3: Use calculator
  - Input: "5000 / 98750"
  - Output: "Result: 0.0506"

Step 4: Reason & Answer
  - "You can buy approximately 0.05 Bitcoin"
```

### What If Agent Gets It Wrong?

**Example**:
```
User: "Calculate Apple Inc's stock price * 2"
Agent: (May use web_search to find Apple stock price)
       (Then use calculator to multiply by 2)
       "Apple stock * 2 = $X"
```

---

## Common Patterns

### Pattern 1: Direct Reasoning
```
Question: "What is Python?"
Response: "Python is a programming language..."
Tools Used: None (LLM answers directly)
```

### Pattern 2: Single Tool
```
Question: "What's trending today?"
Action: web_search("trending today")
Response: Formatted search results
```

### Pattern 3: Sequential Tools
```
Question: "Calculate 30% of today's Bitcoin price"
Action 1: web_search("bitcoin price today")
Action 2: calculator("price * 0.3")
Response: Combined answer
```

### Pattern 4: Conditional Tools
```
Question: "Is Paris the capital of France and 1+1=2?"
Action 1: No web search needed (well-known facts)
Action 2: calculator("1+1") if really needed
Response: "Yes, both are correct"
```

---

## Building Your Own

### Adding a New Tool: Weather

```python
def get_weather(location: str) -> str:
    """Get weather for a location"""
    import requests
    try:
        # Call weather API
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={location}"
        )
        data = response.json()
        return f"Weather in {location}: {data['main']['temp']}°C"
    except Exception as e:
        return f"Error: {str(e)}"

# Add to tools list
weather_tool = Tool(
    name="weather",
    func=get_weather,
    description="Get current weather for any location"
)

tools = [web_search_tool, calculator_tool, weather_tool]
```

### Adding a New Tool: File Reader

```python
def read_file(filename: str) -> str:
    """Read a file's contents"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

# Add to tools
file_tool = Tool(
    name="read_file",
    func=read_file,
    description="Read contents of a file"
)
```

### Adding a New Tool: Database Query

```python
def query_database(sql: str) -> str:
    """Query the database"""
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return str(results)
    except Exception as e:
        return f"Error: {str(e)}"

# Add to tools
db_tool = Tool(
    name="database",
    func=query_database,
    description="Query the database with SQL"
)
```

---

## Key Takeaways

✅ **Agents are decision-makers**: They decide what tools to use
✅ **Tools are extensions**: They let agents do things beyond LLM knowledge
✅ **Descriptions matter**: Good descriptions help agents choose right tools
✅ **Safety first**: Always validate/limit what tools can do
✅ **Chaining works**: Multiple tools can be used in sequence
✅ **Feedback loop**: Agent sees tool results and reasons about them

---

## Visual Summary

```
                  ┌──────────────┐
                  │  User Input  │
                  └──────┬───────┘
                         ↓
                  ┌──────────────┐
                  │ Parse Input  │
                  └──────┬───────┘
                         ↓
              ┌──────────────────────┐
              │ LLM Reasoning        │
              │ "What tools needed?" │
              └────┬──────────────┬──┘
                   ↓              ↓
            ┌────────────┐  ┌────────────┐
            │ Tool 1     │  │ Tool 2     │
            │ Execute    │  │ Execute    │
            └──┬─────────┘  └────┬───────┘
               ↓                 ↓
            ┌────────────────────────┐
            │ Combine Results        │
            │ Final Reasoning        │
            └──────┬────────────────┘
                   ↓
            ┌────────────────────────┐
            │ Response to User       │
            └────────────────────────┘
```

---

## Practice Questions

Try asking your agent these questions and think about which tools it uses:

1. "What's 50 * 50?" → Calculator
2. "What's today's weather?" → Web Search (needs location)
3. "Who is Elon Musk?" → Web Search (for current info)
4. "Calculate 15% of 8000" → Calculator
5. "Tell me about machine learning" → LLM knowledge (no tools)
6. "What's Bitcoin's price in dollars * euros conversion?" → Web Search + Math

---

Happy learning! 🚀
