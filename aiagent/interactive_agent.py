"""
Interactive AI Agent - Chat Interface Version
Better for testing and understanding how agents work
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool
from duckduckgo_search import DDGS

# Load environment variables
load_dotenv()

print("\n" + "="*80)
print("🤖 INTERACTIVE AI AGENT - Learning Edition")
print("="*80 + "\n")

# ===== SETUP =====
print("📡 Initializing agent components...\n")

# Connect to GitHub Models
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=0.7
)

print("✅ Connected to GitHub Models (GPT-4o-mini)\n")


# ===== TOOLS =====
def search_web(query: str) -> str:
    """Search the web for information using DuckDuckGo"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

            if not results:
                return "No results found for your query."

            formatted_results = []
            for i, result in enumerate(results, 1):
                formatted_results.append(
                    f"{i}. {result['title']}\n"
                    f"   Summary: {result['body'][:200]}...\n"
                    f"   Source: {result['href']}\n"
                )

            return "\n".join(formatted_results)
    except Exception as e:
        return f"Search error: {str(e)}"


def calculate(expression: str) -> str:
    """Calculate mathematical expressions safely"""
    try:
        # Safe evaluation - only allows basic math operations
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"


def get_current_time(timezone: str = "UTC") -> str:
    """Get current time in a specific timezone"""
    from datetime import datetime
    try:
        return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error: {str(e)}"


# Create tools
tools = [
    Tool(
        name="web_search",
        func=search_web,
        description="Search the web for current information, news, "
                    "facts. Use when you need up-to-date data."
    ),
    Tool(
        name="calculator",
        func=calculate,
        description="Calculate mathematical expressions. "
                    "Examples: '10 + 5', '100 * 2', '50 / 5'"
    ),
    Tool(
        name="time",
        func=get_current_time,
        description="Get the current time"
    )
]

print(f"✅ Loaded {len(tools)} tools: web_search, calculator, time\n")

# ===== AGENT SETUP =====
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and friendly AI assistant. "
     "You can search the web, do calculations, and tell time.\n\n"
     "Guidelines:\n"
     "1. Be conversational and helpful\n"
     "2. Use tools when needed to find accurate information\n"
     "3. Explain your reasoning\n"
     "4. If you don't know something, say so\n"
     "5. Provide sources when you use web search\n\n"
     "Remember: You're learning to be an AI agent!"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # Shows the thinking process
    handle_parsing_errors=True,
    max_iterations=10
)

print("✅ Agent initialized and ready!\n")
print("="*80)
print("💡 HOW THIS WORKS:")
print("="*80)
print("""
When you ask a question, the agent will:
1. Read your question
2. Decide if it needs to use any tools
3. Use the best tool(s) available
4. Think about the results
5. Give you an answer

You'll see all the thinking steps because verbose=True!
""")
print("="*80 + "\n")


# ===== INTERACTIVE CHAT =====
def chat_with_agent():
    """Interactive chat loop"""
    print("Commands:")
    print("  - Type any question to ask the agent")
    print("  - Type 'exit' or 'quit' to stop")
    print("  - Type 'examples' to see example questions\n")

    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            if not user_input:
                print("Please enter a question.")
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye! Thanks for chatting with me!\n")
                break

            if user_input.lower() == "examples":
                print("""
Example questions you can ask:
1. "What is the capital of France?"
2. "Calculate 1234 * 5678"
3. "What's trending in AI today?"
4. "What time is it?"
5. "Who won the latest World Cup?"
6. "Calculate the square root of 144"
7. "Tell me about machine learning"
                """)
                continue

            print("\n🤖 Agent: (thinking...)\n")
            print("-" * 80)

            response = agent_executor.invoke({"input": user_input})

            print("-" * 80)
            print(f"\n🤖 Agent: {response['output']}\n")

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")
            print("Try asking a simpler question.\n")


# ===== MAIN =====
if __name__ == "__main__":
    try:
        chat_with_agent()
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        print("Make sure your GITHUB_TOKEN is set in .env file")
