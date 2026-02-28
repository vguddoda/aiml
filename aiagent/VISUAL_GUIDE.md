# 📊 AI Agent Visual Learning Guide

## Architecture Diagram

```
                        ┌─────────────────────────────┐
                        │   GitHub Models API         │
                        │   (gpt-4o-mini)             │
                        └──────────────┬──────────────┘
                                       ↑
                                       │ (GITHUB_TOKEN)
                                       │
        ┌──────────────────────────────┼──────────────────────────┐
        │                              │                          │
        │                    ┌─────────▼──────────┐               │
        │                    │  Your AI Agent     │               │
        │                    │                    │               │
        │                    │ - Thinks           │               │
        │                    │ - Reasons          │               │
        │                    │ - Makes Decisions  │               │
        │                    └──────┬──────────┬──┘               │
        │                           │          │                  │
        │              ┌────────────┴──────┬───┴──────┐           │
        │              ↓                   ↓          ↓           │
        │         ┌─────────┐      ┌────────────┐ ┌──────┐       │
        │         │ Tools   │      │ Reasoning  │ │Logic │       │
        │         │         │      │            │ │      │       │
        │         │- Search │      └────────────┘ └──────┘       │
        │         │- Calculate               │                   │
        │         │- Time   │◄───────────────┘                   │
        │         └────┬────┘                                    │
        │              │                                         │
        ├──────────────┼─────────────────────────────────────────┤
        │              │                                         │
   ┌────▼────┐ ┌──────▼──────┐  ┌──────────┐  ┌─────────────┐   │
   │DuckDuckGo        │ Safe Math   │ System    │ Settings  │   │
   │ Search  │      │ Evaluation  │ Time    │ Temperature   │   │
   └─────────┘      └─────────────┘ └──────────┘ └─────────────┘   │
        │                                                        │
        └────────────────────────────────────────────────────────┘
                            ↑
                            │
                    ┌───────▼────────┐
                    │  Your Questions│
                    │  Chat Interface│
                    └────────────────┘
```

## Tool Execution Flow

### Simple Tool Use (Web Search)

```
     Question
         │
         ▼
    ┌────────────────┐
    │ Agent analyzes │
    │ "Need search?" │
    └────────┬───────┘
             │
          YES│
             ▼
    ┌─────────────────────┐
    │ web_search(query)   │
    │                     │
    │ Uses DuckDuckGo API │
    │ Returns results     │
    └────────┬────────────┘
             │
             ▼
    ┌──────────────────┐
    │ Agent sees       │
    │ results          │
    │ Generates answer │
    └────────┬─────────┘
             │
             ▼
        Response
```

### Complex Tool Use (Calculator)

```
     Question: "Calculate 50 * 50"
         │
         ▼
    ┌────────────────┐
    │ Agent analyzes │
    │ "Math problem" │
    └────────┬───────┘
             │
          YES│
             ▼
    ┌────────────────────────┐
    │ calculate("50 * 50")   │
    │                        │
    │ Safe evaluation:       │
    │ eval(expr, {}, {})     │
    │ Returns: 2500          │
    └────────┬───────────────┘
             │
             ▼
    ┌──────────────────┐
    │ Result: 2500     │
    │ Answer user      │
    └────────┬─────────┘
             │
             ▼
    "The answer is 2500"
```

### Multi-Tool Chain

```
Question: "What's 30% of Bitcoin's current price?"
                   │
                   ▼
        ┌────────────────────┐
        │ Agent analyzes     │
        │ "Need web + math"  │
        └────────┬───────────┘
                 │
        ┌────────┴────────┐
        ↓                 ↓
    ┌──────────┐     ┌──────────────┐
    │Step 1    │     │Step 2        │
    │web_search│     │calculator    │
    │("BTC")   │     │"price * 0.3" │
    └────┬─────┘     └────┬─────────┘
         │ Returns        │ Takes result
         │ "$98,750"      │ from Step 1
         │                ↓
         │           29,625
         │                │
         └────────┬───────┘
                  ▼
         ┌─────────────────┐
         │ Combine Results │
         │ "30% of Bitcoin │
         │ is $29,625"     │
         └────────┬────────┘
                  ↓
              Response
```

## Decision Tree - When to Use Tools?

```
                        Question
                           │
                ┌──────────┴──────────┐
                │                     │
            Is it math?          Do I know the
                │                 answer?
             YES│NO               │
              ↓  └─────┐      YES │NO
        ┌─────────┐    │         ↓  ├─┐
        │Use:     │    └──────────┐  │ │
        │calc     │              ↓  ↓ │
        └────┬────┘              OR │ │
             │            ┌─────────┘ │
             │            │           │
             │        Do I need   Is it    │
             │        current     about    │
             │        data?       code?    │
             │        │           │        │
             │      YES│NO       YES│      │
             │        ↓  └────┐    ↓      │
             │        │       │  Use search│
             │        │    ┌──┴──────────┘
             │        │    │
             │  Is it │    │
             │  real- │    │
             │  time? │    │
             │   │    │    │
             │ YES    │    │
             │   ↓    │    │
             │ Use    │    │
             │search  │    │
             │        │    │
             └────┬───┴────┴─┐
                  ↓          ↓
            USE TOOL    ANSWER DIRECTLY
```

## Tool Capability Matrix

```
┌─────────────────┬──────────────┬──────────────┬────────────┐
│ Tool            │ What It Does │ Input        │ Output     │
├─────────────────┼──────────────┼──────────────┼────────────┤
│ web_search      │ Find info    │ Query string │ Results    │
│                 │ online       │ (any topic)  │ with links │
├─────────────────┼──────────────┼──────────────┼────────────┤
│ calculator      │ Do math      │ Expression   │ Number     │
│                 │ safely       │ like "1+2"   │ result     │
├─────────────────┼──────────────┼──────────────┼────────────┤
│ time            │ Get time     │ Timezone     │ Current    │
│                 │ now          │ (optional)   │ timestamp  │
└─────────────────┴──────────────┴──────────────┴────────────┘
```

## Temperature Effect on Responses

```
Temperature = 0.0 (Deterministic)
Question: "What is 2+2?"
Response: "The answer is 4"
Response: "The answer is 4"  ← Always the same
Response: "The answer is 4"

Temperature = 0.5 (Balanced)
Question: "What is 2+2?"
Response: "The answer is 4"
Response: "2 plus 2 equals 4"  ← Slightly varied
Response: "The sum is 4"

Temperature = 1.0 (Creative)
Question: "What is 2+2?"
Response: "Well, if you take two things and add two more..."
Response: "Mathematically speaking, the result is 4"  ← Very varied
Response: "You get four items in total"
```

## Agent Lifecycle

```
START
  │
  ▼
┌─────────────────────────┐
│ 1. Initialize           │
│    - Load LLM           │
│    - Load Tools         │
│    - Set Prompt         │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ 2. Receive Input        │
│    - Wait for question  │
│    - Parse question     │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ 3. LLM Thinking         │
│    - Analyze question   │
│    - Plan response      │
└──────────┬──────────────┘
           │
        ┌──┴──┐
        ↓     ↓
     YES    NO
      │      │
      ↓      ▼
    ┌─────┐ ┌──────────────┐
    │Use  │ │ Generate     │
    │Tool?│ │ Direct Answer│
    └──┬──┘ └────┬─────────┘
       │         │
       ▼         │
    ┌────────┐   │
    │Execute │   │
    │Tool    │   │
    └──┬─────┘   │
       │         │
       └────┬────┘
            ▼
    ┌──────────────────┐
    │ 4. Reasoning     │
    │ - Combine output │
    │ - Think about    │
    │   results        │
    └────────┬─────────┘
             │
             ▼
    ┌────────────────┐
    │ 5. Response    │
    │ - Format answer│
    │ - Return to    │
    │   user         │
    └────────┬───────┘
             │
             ▼
    ┌──────────────────┐
    │ Await Next Input │
    │ (Loop back to 2) │
    └──────────────────┘
```

## Prompt Structure

```
┌──────────────────────────────────────────┐
│ SYSTEM PROMPT                            │
│ "You are a helpful AI assistant..."      │
│ - Defines behavior                       │
│ - Sets tone                              │
│ - Gives instructions                     │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│ MESSAGE HISTORY                          │
│ - Previous messages                      │
│ - Agent's scratchpad (thinking)          │
│ - Tool outputs                           │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│ CURRENT USER MESSAGE                     │
│ "What is 100 * 50?"                      │
└──────────────┬───────────────────────────┘
               │
               ▼
         LLM PROCESSES
         ALL CONTEXT
               │
               ▼
         GENERATES RESPONSE
```

## Error Handling Flow

```
Question arrives
      │
      ▼
┌──────────────┐
│ Parse Input  │
└──────┬───────┘
       │
    ERROR?
      │ YES
      ▼
┌─────────────────────┐
│ Catch Exception     │
│ "Invalid input"     │
└──────┬──────────────┘
       │
       ▼ NO, continue
┌──────────────┐
│ Analyze Q    │
└──────┬───────┘
       │
    TOOL NEEDED?
       │ YES
       ▼
┌──────────────┐
│ Execute Tool │
└──────┬───────┘
       │
    ERROR?
      │ YES
      ▼
┌──────────────────────┐
│ Try/Except Catch     │
│ "Tool Error: ..."    │
│ Return error message │
└──────┬───────────────┘
       │
       ▼ NO, continue
┌──────────────┐
│ Process OK   │
│ Generate     │
│ Response     │
└──────┬───────┘
       │
       ▼
   RETURN ANSWER
```

## Component Relationships

```
                    requirements.txt
                         │
                         ▼
    ┌────────────────────────────────────────┐
    │         PYTHON ENVIRONMENT             │
    │  (langchain, openai, duckduckgo, etc)  │
    └────────────┬─────────────────────────┬─┘
                 │                         │
                 ▼                         ▼
    ┌──────────────────────┐    ┌──────────────────────┐
    │ my_first_agent.py    │    │interactive_agent.py  │
    │                      │    │                      │
    │ - Batch mode         │    │- Chat mode           │
    │ - Predefined Qs      │    │- User input          │
    │ - Learning aid       │    │- Best for learning   │
    └──────────┬───────────┘    └──────────┬───────────┘
               │                           │
               └────────────┬──────────────┘
                            ▼
                   ┌──────────────────┐
                   │  .env File       │
                   │  (Your Token)    │
                   └────────┬─────────┘
                            ▼
                   ┌──────────────────┐
                   │  GitHub Models   │
                   │  (GPT-4o-mini)   │
                   └──────────────────┘
```

## Question Complexity Levels

```
LEVEL 1: Direct Knowledge (No Tools)
Question: "What is Python?"
Agent: Answers from training → No tools used ✓

LEVEL 2: Simple Tool (One Tool)
Question: "Calculate 100 * 50"
Agent: Uses calculator → Returns "5000" ✓

LEVEL 3: Search (One Tool)
Question: "What's trending?"
Agent: Uses web_search → Returns current trends ✓

LEVEL 4: Complex (Multiple Tools)
Question: "What's 30% of Bitcoin's price?"
Agent: web_search → calculator → Combines → Returns answer ✓

LEVEL 5: Reasoning (Logic + Tools)
Question: "Is Python easier than Rust for beginners?"
Agent: web_search (for comparisons) → Reasons → Returns answer ✓
```

---

**Use these diagrams to understand the flow when building or debugging your agent!**
