# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Pennywise is an AI-powered financial advisory application built with Streamlit that provides personalized financial guidance, portfolio analysis, and goal-based planning. The application combines conversational AI, real-time market data, and machine learning recommendations to democratize access to financial advice.

## Common Commands

### Running the Application
```bash
# Run the main application (port 5000)
streamlit run app.py --server.port 5000

# Alternative with default configuration (uses .streamlit/config.toml)
streamlit run app.py
```

### Development Setup
```bash
# Set up virtual environment
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set required environment variable
export OPENAI_API_KEY="your-openai-key-here"
```

### Dependencies Management
```bash
# Install new packages and update requirements
pip install package_name
pip freeze > requirements.txt

# Using pyproject.toml (alternative)
pip install -e .
```

## Architecture Overview

The application follows a modular, layered architecture:

### Application Structure
```
app.py                    # Main Streamlit application and UI orchestration
utils/                    # Business logic modules
├── financial_advisor.py     # AI advice generation (OpenAI GPT-4o)
├── portfolio_analyzer.py    # Investment analysis and risk assessment
├── goal_planner.py          # Financial goal setting and tracking
├── market_data.py           # Real-time market data (Yahoo Finance)
├── recommendation_engine.py # ML-powered investment recommendations
└── user_profile.py          # User data validation and health scoring
```

### Key Architectural Patterns

1. **Session State Management**: User data persists only during Streamlit sessions, no permanent storage
2. **Component Caching**: `@st.cache_resource` decorator used for expensive initializations
3. **API Integration**: OpenAI for AI advice, Yahoo Finance for market data
4. **Fallback Systems**: Mock data generation when external APIs fail
5. **Error Handling**: Graceful degradation with user-friendly error messages

### Data Flow
- User profile creation → Session state → Business logic modules → External APIs → UI updates
- All user data exists only in `st.session_state` during the session
- Components are initialized once using `@st.cache_resource`

## Core Business Logic

### Financial Advisor (`utils/financial_advisor.py`)
- Uses OpenAI GPT-4o model (do not change unless explicitly requested)
- Generates context-aware advice based on user profiles
- Implements comprehensive prompt engineering for financial domain

### Portfolio Analyzer (`utils/portfolio_analyzer.py`)
- Integrates with Yahoo Finance API via `yfinance` library
- Calculates risk metrics: volatility, Sharpe ratio, diversification scores
- Provides rebalancing recommendations based on user risk tolerance

### Goal Planner (`utils/goal_planner.py`)
- Performs inflation-adjusted financial planning calculations
- Assesses goal feasibility based on current financial situation
- Generates timeline and savings requirement analysis

### Market Data Provider (`utils/market_data.py`)
- Real-time data from Yahoo Finance API
- Implements caching for performance optimization
- Fallback to mock data when APIs are unavailable

### Recommendation Engine (`utils/recommendation_engine.py`)
- K-means clustering for user segmentation
- Collaborative filtering based on similar user profiles
- Risk-appropriate investment product recommendations

### User Profile Manager (`utils/user_profile.py`)
- Comprehensive data validation and sanitization
- Financial health scoring algorithm
- User segmentation for personalized recommendations

## Configuration Files

### Streamlit Configuration (`.streamlit/config.toml`)
- Configured for headless mode on port 5000
- Light theme with usage stats disabled
- Optimized for cloud deployment

### Dependencies (`requirements.txt` & `pyproject.toml`)
- Core: `streamlit>=1.47.1`, `openai>=1.96.0`, `pandas>=2.3.1`
- Data: `yfinance>=0.2.65`, `numpy>=2.3.2`, `plotly>=6.2.0`
- ML: `scikit-learn>=1.7.0`, `anthropic>=0.59.0`

## Environment Variables

### Required
- `OPENAI_API_KEY`: OpenAI API key for AI advice generation

### Optional
- `ANTHROPIC_API_KEY`: Backup AI service (currently unused but supported)

## Security Considerations

- No persistent data storage - all user data is session-only
- API keys stored in environment variables, never in code
- Comprehensive input validation and sanitization
- Session isolation prevents data sharing between users
- Minimal data collection approach

## Development Guidelines

### Code Organization
- Each utility module handles a single domain (financial advice, portfolio analysis, etc.)
- Consistent error handling with user-friendly messages
- Modular design with loose coupling between components

### Adding New Features
1. Create new utility modules in `utils/` for business logic
2. Import and initialize in `app.py` using `@st.cache_resource`
3. Add UI components following existing patterns
4. Update session state management as needed
5. Implement proper error handling and fallbacks

### API Integration
- Always implement fallback mechanisms for external API failures
- Use try-catch blocks with graceful degradation
- Provide clear user feedback when APIs are unavailable
- Consider rate limiting and caching strategies

## Testing and Validation

The application uses mock data in `data/mock_users.py` for ML model training and testing. When developing:
- Test with various user profiles and risk tolerances
- Verify API fallbacks work correctly
- Ensure session state management works across page navigation
- Test with and without API keys to verify fallback behavior

## Performance Optimization

- Component initialization cached with `@st.cache_resource`
- Market data requests batched when possible
- Efficient data structures using pandas for data manipulation
- Lazy loading of expensive operations

## Deployment Notes

The application is optimized for cloud deployment (currently on Replit) but supports local development. The Streamlit configuration handles headless mode and port binding automatically.