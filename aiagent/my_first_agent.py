"""
My First AI Agent - A Simple Web Search Assistant
This agent can search the web and answer questions.
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

print("🚀 Starting My First AI Agent...\n")

# ===== STEP 1: Connect to GitHub Models =====
print("📡 Connecting to GitHub Models...")

llm = ChatOpenAI(
    model="gpt-4o-mini",  # Fast and free tier friendly!
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
    temperature=0.7
)

print("✅ Connected to GPT-4o-mini\n")

# ===== STEP 2: Create Tools =====
print("🔧 Creating tools for the agent...")

def search_web(query: str) -> str:
    """
    Search the web using DuckDuckGo (free, no API key needed!)
    
    Args:
        query: The search query string
        
    Returns:
        Formatted search results
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            
            if not results:
                return "No results found."
            
            formatted_results = []
            for i, result in enumerate(results, 1):
                formatted_results.append(
                    f"{i}. **{result['title']}**\n"
                    f"   {result['body']}\n"
                    f"   Source: {result['href']}\n"
                )
            
            return "\n".join(formatted_results)
    except Exception as e:
        return f"Search error: {str(e)}"

def calculate(expression: str) -> str:
    """
    Calculate mathematical expressions
    
    Args:
        expression: Math expression like "2 + 2" or "10 * 5"
        
    Returns:
        The calculated result
    """
    try:
        # Safe evaluation of math expressions
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

# Create tool objects
web_search_tool = Tool(
    name="web_search",
    func=search_web,
    description="Search the web for current information, news, facts, or any real-time data. Use this when you need up-to-date information."
)

calculator_tool = Tool(
    name="calculator",
    func=calculate,
    description="Calculate mathematical expressions. Use for any math calculations like addition, subtraction, multiplication, division."
)

tools = [web_search_tool, calculator_tool]

print(f"✅ Created {len(tools)} tools: web_search, calculator\n")

# ===== STEP 3: Create Agent Prompt =====
print("💭 Setting up agent behavior...")

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI assistant that can search the web and do calculations.

When answering questions:
1. Think about what information you need
2. Use your tools when necessary
3. Provide clear, accurate answers with sources
4. If you're not sure, say so

Be conversational and helpful!"""),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

print("✅ Agent personality configured\n")

# ===== STEP 4: Create the Agent =====
print("🤖 Building the agent...")

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # Shows thinking process
    handle_parsing_errors=True
)

print("✅ Agent ready!\n")

# ===== STEP 5: Run the Agent =====
def ask_agent(question: str):
    """
    Ask the agent a question
    
    Args:
        question: Your question for the agent
        
    Returns:
        The agent's response
    """
    print(f"❓ Question: {question}\n")
    print("🧠 Agent is thinking...\n")
    print("-" * 80)
    
    try:
        response = agent_executor.invoke({"input": question})
        return response["output"]
    except Exception as e:
        return f"Error: {str(e)}"

# ===== STEP 6: Test It! =====
if __name__ == "__main__":
    print("=" * 80)
    print("🎉 MY FIRST AI AGENT IS RUNNING!")
    print("=" * 80)
    print()
    
    # Test questions
    test_questions = [
        "What is the current NIFTY 50 index value?",
        "Calculate 1234 * 5678",
        "Who won the latest cricket match between India and Australia?"
    ]
    
    for question in test_questions:
        answer = ask_agent(question)
        print("-" * 80)
        print(f"\n✅ ANSWER:\n{answer}\n")
        print("=" * 80)
        print()
        
        # Wait for user to press enter before next question
        input("Press Enter to continue to next question...")
        print()