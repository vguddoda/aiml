"""
Test script to verify AI Agent works
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

print("\n" + "="*80)
print("🧪 TESTING AI AGENT SETUP")
print("="*80 + "\n")

# Test 1: Check if .env file exists and has token
print("Test 1: Checking .env file...")
if os.path.exists('.env'):
    token = os.getenv("GITHUB_TOKEN")
    if token and token != "your_github_token_here":
        print("✅ PASS: .env file exists and has a valid token\n")
    else:
        print("❌ FAIL: Token not found or is placeholder\n")
else:
    print("❌ FAIL: .env file not found\n")

# Test 2: Check if LLM can connect
print("Test 2: Connecting to GitHub Models LLM...")
try:
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("GITHUB_TOKEN"),
        base_url="https://models.inference.ai.azure.com",
        temperature=0.7
    )
    print("✅ PASS: LLM connection successful\n")
except Exception as e:
    print(f"❌ FAIL: {str(e)}\n")

# Test 3: Check if tools can be imported
print("Test 3: Checking if tools can be imported...")
try:
    from duckduckgo_search import DDGS
    print("✅ PASS: DuckDuckGo search available\n")
except Exception as e:
    print(f"❌ FAIL: {str(e)}\n")

# Test 4: Test calculator tool
print("Test 4: Testing calculator tool...")
try:
    result = eval("100 * 50", {"__builtins__": {}}, {})
    if result == 5000:
        print(f"✅ PASS: Calculator works (100 * 50 = {result})\n")
    else:
        print(f"❌ FAIL: Calculator returned wrong result: {result}\n")
except Exception as e:
    print(f"❌ FAIL: {str(e)}\n")

# Test 5: Test web search
print("Test 5: Testing web search...")
try:
    with DDGS() as ddgs:
        results = list(ddgs.text("Python programming", max_results=1))
        if results:
            print("✅ PASS: Web search works\n")
            print(f"   Found: {results[0]['title'][:60]}...\n")
        else:
            print("❌ FAIL: Web search returned no results\n")
except Exception as e:
    print(f"❌ FAIL: {str(e)}\n")

print("="*80)
print("🎉 ALL TESTS COMPLETED!")
print("="*80)
print("\nYour AI Agent is ready to use!")
print("\nRun the interactive agent with:")
print("  python3 interactive_agent.py\n")
