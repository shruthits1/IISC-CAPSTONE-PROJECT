# AI Financial Advisory Platform - Setup Guide

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Keys Setup](#api-keys-setup)
- [Running the Application](#running-the-application)
- [Development Setup](#development-setup)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### System Requirements
- Python 3.11 or higher
- 4GB+ RAM (recommended)
- Internet connection for API access and market data

### Required Accounts
1. **OpenAI Account** (Primary AI service)
   - Visit: https://platform.openai.com/
   - Create account and generate API key
   - Free tier available, pay-per-use pricing

2. **Anthropic Account** (Backup AI service - Optional)
   - Visit: https://console.anthropic.com/
   - Create account and generate API key
   - Free tier available

## Installation

### Option 1: Quick Start (Replit - Recommended)
```bash
# Clone/fork the repository on Replit
# Dependencies are automatically installed
```

### Option 2: Local Development
```bash
# Clone the repository
git clone <repository-url>
cd ai-financial-advisory

# Create virtual environment (recommended)
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install streamlit>=1.46.1 \
           openai>=1.96.0 \
           anthropic>=0.57.1 \
           scikit-learn>=1.7.0 \
           pandas>=2.3.1 \
           numpy>=2.3.1 \
           plotly>=6.2.0 \
           yfinance>=0.2.65
```

### Option 3: Using pip with pyproject.toml
```bash
pip install -e .
```

## Configuration

### Streamlit Configuration
The application includes a pre-configured `.streamlit/config.toml` file:

```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
```

**Important**: Do not modify the server settings as they are optimized for deployment.

## API Keys Setup

### Step 1: Obtain API Keys

#### OpenAI API Key (Required)
1. Visit https://platform.openai.com/api-keys
2. Sign up/log in to your account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. **Important**: Save it securely - you won't see it again

#### Anthropic API Key (Optional)
1. Visit https://console.anthropic.com/
2. Sign up/log in to your account
3. Navigate to API Keys section
4. Generate new key
5. Copy and save securely

### Step 2: Set Environment Variables

#### On Replit
1. Go to Secrets tab in your Repl
2. Add the following secrets:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `ANTHROPIC_API_KEY`: Your Anthropic API key (optional)

#### Local Development
```bash
# Option 1: Export in terminal
export OPENAI_API_KEY="your-openai-key-here"
export ANTHROPIC_API_KEY="your-anthropic-key-here"

# Option 2: Create .env file (recommended)
echo "OPENAI_API_KEY=your-openai-key-here" > .env
echo "ANTHROPIC_API_KEY=your-anthropic-key-here" >> .env

# Option 3: Add to your shell profile (~/.bashrc, ~/.zshrc)
echo 'export OPENAI_API_KEY="your-openai-key-here"' >> ~/.bashrc
```

## Running the Application

### Start the Application
```bash
streamlit run app.py --server.port 5000
```

### Access the Application
- **Local**: http://localhost:5000
- **Replit**: Your repl's URL (e.g., https://your-repl-name.your-username.replit.app)

### First Time Usage
1. Click "Setup Profile" in the sidebar
2. Fill out your financial profile:
   - Personal information (name, age, income)
   - Risk tolerance and investment experience
   - Financial goals and current savings
3. Save your profile
4. Explore the different features:
   - **Dashboard**: Overview of your financial health
   - **AI Chat**: Ask personalized financial questions
   - **Portfolio Analysis**: Analyze your investments
   - **Goal Planning**: Set and track financial goals
   - **Market Insights**: Current market data and trends

## Development Setup

### Project Structure
```
ai-financial-advisory/
├── app.py                 # Main Streamlit application
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── utils/                # Core business logic
│   ├── financial_advisor.py      # AI-powered advice
│   ├── portfolio_analyzer.py     # Portfolio analysis
│   ├── goal_planner.py          # Financial goal planning
│   ├── market_data.py           # Market data provider
│   ├── recommendation_engine.py # ML recommendations
│   └── user_profile.py          # User profile management
├── data/
│   └── mock_users.py            # Test data for ML
├── docs/                        # Documentation
└── pyproject.toml              # Dependencies
```

### Code Quality and Testing
```bash
# Format code (if using black)
black app.py utils/ data/

# Type checking (if using mypy)
mypy app.py utils/ data/

# Run basic functionality test
python -c "from utils.financial_advisor import FinancialAdvisor; print('Import test passed')"
```

### Adding New Features
1. Create new utility modules in `utils/` directory
2. Import and initialize in `app.py`
3. Add UI components using Streamlit
4. Update documentation

## Troubleshooting

### Common Issues

#### 1. "Module not found" errors
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt  # or follow installation steps above
```

#### 2. API Key errors
- Verify API keys are correctly set in environment variables
- Check that keys are valid and have sufficient credits
- For Replit: Check the Secrets tab

#### 3. Market data errors
- yfinance may occasionally fail - the app includes fallback mock data
- Check internet connection
- Yahoo Finance API limits may apply

#### 4. Port already in use
```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9

# Or use a different port
streamlit run app.py --server.port 8501
```

#### 5. Streamlit caching issues
```bash
# Clear Streamlit cache
streamlit cache clear
```

### Performance Optimization
- Market data is cached to reduce API calls
- User profiles are stored in session state
- Large computations use Streamlit's caching decorators

### Security Notes
- Never commit API keys to version control
- Use environment variables for sensitive data
- The application doesn't store personal financial data permanently
- All data remains in browser session only

### Getting Help
1. Check the error messages in the terminal/console
2. Verify all prerequisites are met
3. Ensure API keys are valid and properly configured
4. Review the application logs for detailed error information

### Development Tips
- Use Streamlit's hot reload: save files and see changes immediately
- Enable debug mode: `streamlit run app.py --logger.level debug`
- Use browser developer tools to debug frontend issues
- Monitor API usage to avoid hitting rate limits