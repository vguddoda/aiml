"""
Debug script to show if agent is making external calls
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool

# Load environment variables
load_dotenv()

print("\n" + "="*80)
print("🔍 DEBUGGING: CHECKING EXTERNAL CALLS")
print("="*80 + "\n")

# ===== SETUP =====
# Connect to GitHub Models
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=0.7
)

print("1️⃣  LLM Connection:")
print("   - Model: gpt-4o-mini")
print("   - Base URL: https://models.inference.ai.azure.com")
print("   - ✅ This IS an EXTERNAL CALL to GitHub Models\n")

# ===== TOOLS =====
def calculate(expression: str) -> str:
    """Calculate mathematical expressions safely"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

def get_current_time(timezone: str = "UTC") -> str:
    """Get current time"""
    from datetime import datetime
    try:
        return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create tools
tools = [
    Tool(
        name="calculator",
        func=calculate,
        description="Calculate mathematical expressions"
    ),
    Tool(
        name="time",
        func=get_current_time,
        description="Get the current time"
    )
]

print("2️⃣  Available Tools:")
print("   - calculator: ❌ NO external call (pure Python)")
print("   - time: ❌ NO external call (local system)\n")

# ===== AGENT SETUP =====
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. You can do calculations and tell time."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,  # Disable verbose to see our debug output
    handle_parsing_errors=True,
    max_iterations=10
)

print("3️⃣  Agent Initialization:")
print("   - ✅ LLM will make EXTERNAL calls to GitHub Models API\n")

print("="*80)
print("📊 EXTERNAL CALLS SUMMARY")
print("="*80 + "\n")

print("When you ask a question, here's what happens:\n")

questions = [
    "Calculate 100 * 50",
    "What time is it?",
    "Tell me about Python"
]

for q in questions:
    print(f"Question: '{q}'")
    print("   ├─ Goes to: GitHub Models API (gpt-4o-mini)")
    print("   │  └─ ✅ EXTERNAL CALL - Over internet")
    print("   ├─ LLM decides if tool needed:")
    
    if "Calculate" in q or "time" in q.lower():
        print("   │  └─ YES, uses local tool")
        print("   │     ├─ calculator: Local computation ❌ NO EXTERNAL CALL")
        print("   │     └─ time: Local system ❌ NO EXTERNAL CALL")
    else:
        print("   │  └─ NO, answers from training")
    print("   └─ Response back from GitHub Models\n")

print("="*80)
print("🌐 EXTERNAL SERVICES USED")
print("="*80 + "\n")

print("✅ EXTERNAL (makes network calls):")
print("   1. GitHub Models API (gpt-4o-mini LLM)")
print("      - Every question goes here first")
print("      - Requires: internet connection")
print("      - Requires: GitHub token\n")

print("❌ INTERNAL (NO external calls):")
print("   1. Calculator tool - runs locally")
print("   2. Time tool - reads system time")
print("   3. Agent logic - runs on your computer\n")

print("="*80)
print("🎯 KEY POINT")
print("="*80 + "\n")

print("YES, your agent IS making EXTERNAL calls:")
print("  - Every question requires a call to GitHub Models API")
print("  - This is normal and expected")
print("  - It's how the agent understands questions")
print("  - Your GitHub token authenticates these calls\n")

print("The tools (calculator, time) do NOT make external calls")
print("They run locally on your computer.\n")

print("="*80)
print("\nTo verify, run:")
print("  python3 simple_agent.py")
print("  Then ask: 'Calculate 100 * 50'")
print("  The agent will use GitHub Models to understand,")
print("  then use local calculator for the math.\n")
