# AI Financial Advisory Platform - API Reference

## Overview

This document provides detailed information about the internal APIs and interfaces of the AI Financial Advisory Platform. Each utility module exposes a clean interface for specific financial functionalities.

## Core Components

### Financial Advisor (`utils/financial_advisor.py`)

#### Class: `FinancialAdvisor`

**Purpose**: Provides AI-powered personalized financial advice using OpenAI's GPT-4o model.

##### Methods

```python
def __init__(self)
```
- **Description**: Initialize the Financial Advisor with OpenAI client
- **Parameters**: None
- **Environment Variables Required**: `OPENAI_API_KEY`

```python
def get_personalized_advice(self, user_query: str, user_profile: dict) -> str
```
- **Description**: Generate personalized financial advice based on user query and profile
- **Parameters**:
  - `user_query` (str): The financial question or topic from the user
  - `user_profile` (dict): Complete user profile with financial information
- **Returns**: Personalized advice as formatted string
- **Example**:
  ```python
  advisor = FinancialAdvisor()
  advice = advisor.get_personalized_advice(
      "Should I invest in stocks?", 
      user_profile
  )
  ```

```python
def get_quick_insights(self, user_profile: dict) -> list
```
- **Description**: Generate quick financial insights based on user profile
- **Parameters**:
  - `user_profile` (dict): User's financial profile data
- **Returns**: List of insight strings
- **Insights Include**:
  - Savings rate analysis
  - Debt-to-income ratio assessment
  - Emergency fund evaluation
  - Age-appropriate recommendations

```python
def get_risk_assessment(self, user_profile: dict) -> dict
```
- **Description**: Assess user's financial risk profile
- **Parameters**:
  - `user_profile` (dict): User's financial and demographic data
- **Returns**: Dictionary containing:
  - `risk_score` (float): Risk score from 1-10
  - `risk_factors` (dict): Breakdown of risk components
  - `recommendation` (str): Investment strategy recommendation

---

### Portfolio Analyzer (`utils/portfolio_analyzer.py`)

#### Class: `PortfolioAnalyzer`

**Purpose**: Analyze investment portfolios for risk, performance, and optimization opportunities.

##### Methods

```python
def __init__(self)
```
- **Description**: Initialize with default risk-free rate assumption
- **Attributes**: `risk_free_rate = 0.03` (3% assumption)

```python
def analyze_portfolio(self, portfolio_data: dict, user_profile: dict) -> dict
```
- **Description**: Complete portfolio analysis including risk and diversification
- **Parameters**:
  - `portfolio_data` (dict): Portfolio composition with stocks, bonds, cash, etc.
  - `user_profile` (dict): User's risk tolerance and preferences
- **Portfolio Data Format**:
  ```python
  {
      'stocks': {'AAPL': 1000, 'GOOGL': 2000},
      'bonds': 5000,
      'cash': 2000,
      'real_estate': 10000,
      'crypto': 1000
  }
  ```
- **Returns**: Comprehensive analysis dictionary:
  ```python
  {
      'total_value': float,
      'risk_score': float,  # 1-10 scale
      'diversification_score': float,  # 1-10 scale
      'risk_assessment': str,
      'recommendations': list,
      'allocation': dict,
      'metrics': dict
  }
  ```

```python
def get_stock_performance(self, symbols: list, days: int = 30) -> list
```
- **Description**: Get historical stock performance data for visualization
- **Parameters**:
  - `symbols` (list): List of stock symbols (e.g., ['AAPL', 'GOOGL'])
  - `days` (int): Number of days of historical data (default: 30)
- **Returns**: List of performance data dictionaries for charting

---

### Goal Planner (`utils/goal_planner.py`)

#### Class: `GoalPlanner`

**Purpose**: Create and manage financial goal plans with timeline and strategy recommendations.

##### Methods

```python
def __init__(self)
```
- **Description**: Initialize with default inflation and market return assumptions
- **Attributes**:
  - `inflation_rate = 0.03` (3% annual inflation)
  - `market_return = 0.07` (7% average market return)

```python
def create_goal_plan(self, goal_name: str, target_amount: float, 
                    timeline_years: float, priority: str, 
                    user_profile: dict) -> dict
```
- **Description**: Create comprehensive goal plan with feasibility analysis
- **Parameters**:
  - `goal_name` (str): Name/description of the financial goal
  - `target_amount` (float): Target dollar amount needed
  - `timeline_years` (float): Years to achieve the goal
  - `priority` (str): 'High', 'Medium', or 'Low'
  - `user_profile` (dict): User's financial profile
- **Returns**: Complete goal plan dictionary:
  ```python
  {
      'goal_name': str,
      'target_amount': float,
      'future_value_needed': float,  # Inflation-adjusted
      'timeline_years': float,
      'monthly_savings_needed': float,
      'feasibility': str,
      'recommendations': list,
      'investment_strategy': dict,
      'priority': str
  }
  ```

```python
def calculate_goal_progress(self, current_amount: float, 
                           monthly_contribution: float,
                           timeline_remaining: float, 
                           target_amount: float) -> dict
```
- **Description**: Track progress toward financial goal
- **Parameters**: Current savings state and goal parameters
- **Returns**: Progress analysis with projections and status

```python
def optimize_multiple_goals(self, goals: list, user_profile: dict) -> dict
```
- **Description**: Optimize savings allocation across multiple goals
- **Parameters**:
  - `goals` (list): List of goal plan dictionaries
  - `user_profile` (dict): User's available savings capacity
- **Returns**: Allocation optimization plan

---

### Market Data Provider (`utils/market_data.py`)

#### Class: `MarketDataProvider`

**Purpose**: Fetch and process real-time market data with fallback capabilities.

##### Methods

```python
def __init__(self)
```
- **Description**: Initialize with predefined market indices and sectors
- **Data Sources**: Yahoo Finance API via yfinance library

```python
def get_market_overview(self) -> dict
```
- **Description**: Get current market overview with major indices
- **Parameters**: None
- **Returns**: Dictionary of market data:
  ```python
  {
      'S&P 500': {
          'current_price': float,
          'change': float,  # Percentage change
          'prices': list    # 30-day price history
      },
      'Dow Jones': {...},
      'NASDAQ': {...}
  }
  ```

```python
def get_stock_price(self, symbol: str) -> dict
```
- **Description**: Get current stock price and basic information
- **Parameters**: `symbol` (str): Stock ticker symbol
- **Returns**: Stock data dictionary with price, change, and volume

```python
def get_sector_performance(self) -> dict
```
- **Description**: Get performance data for major market sectors
- **Returns**: Sector performance percentages (1-month)

```python
def get_market_insights(self) -> list
```
- **Description**: Generate market insights based on current data
- **Returns**: List of market analysis strings

```python
def get_economic_indicators(self) -> dict
```
- **Description**: Get key economic indicators
- **Returns**: Dictionary with Fed funds rate, treasury yields, unemployment, inflation

```python
def get_crypto_prices(self) -> dict
```
- **Description**: Get major cryptocurrency prices
- **Returns**: Crypto price data for BTC, ETH, ADA, DOT

```python
def get_bond_yields(self) -> dict
```
- **Description**: Get current bond yields for different maturities
- **Returns**: Treasury yield data (10-year, 5-year, 30-year)

---

### Recommendation Engine (`utils/recommendation_engine.py`)

#### Class: `RecommendationEngine`

**Purpose**: Generate personalized investment recommendations using machine learning algorithms.

##### Methods

```python
def __init__(self)
```
- **Description**: Initialize with investment product database and ML components
- **Components**: K-means clustering, StandardScaler, product databases

```python
def get_personalized_recommendations(self, user_profile: dict, 
                                   recommendation_type: str = 'investment') -> dict
```
- **Description**: Get personalized recommendations based on user profile
- **Parameters**:
  - `user_profile` (dict): Complete user profile
  - `recommendation_type` (str): 'investment', 'insurance', or 'comprehensive'
- **Returns**: Recommendation dictionary:
  ```python
  {
      'recommendations': list,      # Top product recommendations
      'portfolio_suggestions': dict,  # Asset allocation suggestions
      'next_steps': list           # Actionable next steps
  }
  ```

```python
def generate_user_segments(self, user_profiles: list) -> dict
```
- **Description**: Segment users for collaborative filtering
- **Parameters**: List of user profiles for clustering
- **Returns**: User segment assignments

```python
def get_collaborative_recommendations(self, user_profile: dict, 
                                    all_user_profiles: list) -> list
```
- **Description**: Get recommendations based on similar users
- **Parameters**: Target user and database of all user profiles
- **Returns**: Collaborative filtering recommendations

---

### User Profile Manager (`utils/user_profile.py`)

#### Class: `UserProfile`

**Purpose**: Manage user profiles with validation, scoring, and analytics.

##### Methods

```python
def __init__(self)
```
- **Description**: Initialize with validation rules and scoring mappings

```python
def validate_profile(self, profile_data: dict) -> tuple[bool, list]
```
- **Description**: Validate user profile data
- **Parameters**: `profile_data` (dict): Raw profile data from forms
- **Returns**: Tuple of (is_valid: bool, errors: list)

```python
def create_profile(self, profile_data: dict) -> dict
```
- **Description**: Create new user profile with validation and defaults
- **Parameters**: Raw profile data dictionary
- **Returns**: Complete validated profile with metadata
- **Raises**: `ValueError` if validation fails

```python
def update_profile(self, existing_profile: dict, updates: dict) -> dict
```
- **Description**: Update existing profile with new data
- **Parameters**: Current profile and update dictionary
- **Returns**: Updated and validated profile

```python
def calculate_financial_health_score(self, profile: dict) -> dict
```
- **Description**: Calculate comprehensive financial health score
- **Parameters**: Complete user profile
- **Returns**: Detailed scoring breakdown:
  ```python
  {
      'overall_score': float,       # 0-100 percentage
      'rating': str,               # Excellent/Good/Fair/Poor
      'color': str,                # UI color coding
      'total_points': float,
      'max_points': int,
      'components': dict,          # Detailed component scores
      'recommendations': list      # Improvement recommendations
  }
  ```

```python
def get_user_segment(self, profile: dict) -> str
```
- **Description**: Categorize user into demographic/financial segment
- **Returns**: Segment name (e.g., "Young Professional", "Conservative Saver")

```python
def compare_profiles(self, profile1: dict, profile2: dict) -> dict
```
- **Description**: Compare two user profiles
- **Returns**: Comparison analysis with similarities and differences

```python
def export_profile(self, profile: dict, format: str = 'json') -> str
```
- **Description**: Export user profile in specified format
- **Parameters**: Profile data and format ('json' or 'summary')
- **Returns**: Formatted profile string

```python
def get_profile_analytics(self, profiles: list) -> dict
```
- **Description**: Generate analytics across multiple user profiles
- **Parameters**: List of user profiles for analysis
- **Returns**: Statistical overview and insights

---

## Data Models

### User Profile Schema

```python
{
    # Required fields
    'name': str,
    'age': int,                    # 18-100
    'annual_income': float,        # >= 0
    'employment_status': str,      # Employed/Self-Employed/Unemployed/Retired/Student
    'risk_tolerance': str,         # Conservative/Moderate/Aggressive
    'investment_experience': str,  # Beginner/Intermediate/Advanced
    'monthly_savings': float,      # >= 0
    
    # Optional fields
    'debt_amount': float,          # >= 0, default: 0
    'financial_goals': list,       # List of goal strings
    'created_date': str,           # ISO format timestamp
    'last_updated': str,           # ISO format timestamp
    'profile_id': str              # Generated unique identifier
}
```

### Portfolio Data Schema

```python
{
    'stocks': dict,        # {'SYMBOL': amount, ...}
    'bonds': float,        # Bond allocation amount
    'cash': float,         # Cash allocation amount
    'real_estate': float,  # Real estate allocation amount
    'crypto': float        # Cryptocurrency allocation amount
}
```

## Error Handling

### Common Exceptions

- **API Failures**: All external API calls include fallback mechanisms
- **Validation Errors**: User input validation with descriptive error messages
- **Missing Dependencies**: Graceful degradation when optional features unavailable
- **Rate Limiting**: Automatic retry mechanisms for API calls

### Error Response Format

```python
{
    'success': bool,
    'error_message': str,
    'error_code': str,
    'fallback_data': dict  # When applicable
}
```

## Performance Considerations

### Caching Strategy

- **Component Level**: `@st.cache_resource` for expensive initializations
- **Function Level**: `@st.cache_data` for data processing operations
- **Session Level**: Streamlit session state for user data persistence

### Rate Limiting

- **Yahoo Finance**: Built-in throttling in yfinance library
- **OpenAI API**: Automatic retry with exponential backoff
- **Batch Operations**: Multiple API calls optimized where possible

## Security Guidelines

### API Key Management

- **Environment Variables**: All API keys stored in environment variables
- **No Hardcoding**: Never commit API keys to version control
- **Validation**: API key presence validated at startup

### Data Privacy

- **No Persistence**: User data not stored permanently
- **Session Isolation**: User data isolated to individual sessions
- **Input Sanitization**: All user inputs validated and sanitized

## Testing Guidelines

### Unit Testing Example

```python
import unittest
from utils.user_profile import UserProfile

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.profile_manager = UserProfile()
    
    def test_profile_validation(self):
        valid_profile = {
            'name': 'John Doe',
            'age': 30,
            'annual_income': 50000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Beginner',
            'monthly_savings': 500
        }
        is_valid, errors = self.profile_manager.validate_profile(valid_profile)
        self.assertTrue(is_valid)
        self.assertEqual(len(errors), 0)
```

### Integration Testing

```python
def test_api_integration():
    """Test external API integration with fallback"""
    from utils.market_data import MarketDataProvider
    
    provider = MarketDataProvider()
    market_data = provider.get_market_overview()
    
    # Should always return data (real or mock)
    assert isinstance(market_data, dict)
    assert len(market_data) > 0
```

## Version Compatibility

### Python Version
- **Minimum**: Python 3.11
- **Recommended**: Python 3.11+

### Dependency Versions
- **Streamlit**: >= 1.46.1
- **OpenAI**: >= 1.96.0
- **Pandas**: >= 2.3.1
- **NumPy**: >= 2.3.1
- **Plotly**: >= 6.2.0
- **Scikit-learn**: >= 1.7.0
- **yfinance**: >= 0.2.65

### API Compatibility

- **OpenAI API**: Compatible with GPT-4o model
- **Yahoo Finance**: Uses yfinance library (unofficial API)
- **Anthropic API**: Optional backup service

---

This API reference provides comprehensive documentation for developers working with the AI Financial Advisory Platform. Each component is designed to be modular and independently testable while maintaining clean interfaces for integration.