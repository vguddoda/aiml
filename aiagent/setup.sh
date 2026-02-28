#!/usr/bin/env bash
# Setup script for AI Agent Development

echo "🚀 Setting up AI Agent Environment..."
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $python_version"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if .env exists
echo ""
if [ ! -f .env ]; then
    echo "⚠️  .env file not found"
    echo "📝 Creating .env from template..."
    cp .env.example .env
    echo "✅ .env created. Please edit it with your GITHUB_TOKEN"
    echo ""
    echo "Get your GitHub token from:"
    echo "  https://github.com/settings/tokens?type=beta"
    echo ""
else
    echo "✅ .env file exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your GITHUB_TOKEN"
echo "2. Run: python my_first_agent.py"
echo "3. Or try: python interactive_agent.py"
echo ""
