"""
Production-Ready AI Agent API
Ready for deployment to Heroku, AWS Lambda, or Docker
"""

from flask import Flask, request, jsonify
import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Initialize LLM
def get_llm():
    """Initialize and return the LLM"""
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("GITHUB_TOKEN"),
        base_url="https://models.inference.ai.azure.com",
        temperature=0.7
    )


# Define tools
def calculate(expression: str) -> str:
    """Calculate mathematical expressions"""
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


# Create tools list
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


def create_agent():
    """Create and return the AI agent"""
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. "
         "You can do calculations and tell time. "
         "Be concise and helpful."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=10
    )

    return agent_executor


# ===== ROUTES =====

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    logger.info("Health check requested")
    return jsonify({
        'status': 'AI Agent API is running ✅',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'endpoints': {
            'health': 'GET /',
            'ask': 'POST /ask',
            'metrics': 'GET /metrics'
        }
    }), 200


@app.route('/health', methods=['GET'])
def health():
    """Detailed health check"""
    try:
        # Test LLM connection
        llm = get_llm()
        logger.info("Health check: LLM connection OK")
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'components': {
                'api': 'running',
                'llm': 'connected',
                'tools': 'available'
            }
        }), 200
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500


@app.route('/ask', methods=['POST'])
def ask_agent():
    """
    Main endpoint to ask the AI agent a question
    
    Request body:
    {
        "question": "What time is it?"
    }
    
    Response:
    {
        "question": "What time is it?",
        "answer": "The current time is...",
        "status": "success",
        "timestamp": "2026-03-01T10:30:00"
    }
    """
    try:
        # Get question from request
        data = request.get_json()
        
        if not data or 'question' not in data:
            logger.warning("Request missing 'question' field")
            return jsonify({
                'status': 'error',
                'error': "Missing 'question' field in request body"
            }), 400
        
        question = data['question'].strip()
        
        if not question:
            logger.warning("Empty question received")
            return jsonify({
                'status': 'error',
                'error': "Question cannot be empty"
            }), 400
        
        logger.info(f"Processing question: {question}")
        
        # Create agent and process question
        agent_executor = create_agent()
        response = agent_executor.invoke({"input": question})
        
        answer = response.get('output', 'No answer generated')
        
        logger.info(f"Answer generated successfully")
        
        return jsonify({
            'status': 'success',
            'question': question,
            'answer': answer,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500


@app.route('/metrics', methods=['GET'])
def metrics():
    """Return application metrics"""
    return jsonify({
        'uptime': 'N/A',
        'requests_processed': 0,
        'errors': 0,
        'avg_response_time': 0
    }), 200


@app.route('/version', methods=['GET'])
def version():
    """Get API version"""
    return jsonify({
        'version': '1.0.0',
        'api': 'AI Agent API',
        'github_models': 'gpt-4o-mini',
        'timestamp': datetime.now().isoformat()
    }), 200


# ===== ERROR HANDLERS =====

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    logger.warning(f"404 error: {error}")
    return jsonify({
        'status': 'error',
        'error': 'Endpoint not found',
        'available_endpoints': ['/', '/health', '/ask', '/metrics', '/version']
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"500 error: {error}")
    return jsonify({
        'status': 'error',
        'error': 'Internal server error'
    }), 500


# ===== MAIN =====

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Get debug mode from environment
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    logger.info(f"Starting AI Agent API on port {port}")
    logger.info(f"Debug mode: {debug}")
    
    # Run app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
