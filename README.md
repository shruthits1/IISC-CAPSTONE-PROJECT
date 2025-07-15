# 🏦 AI Financial Advisory Platform

A comprehensive AI-powered financial advisory application that democratizes access to personalized financial guidance through conversational AI, portfolio analysis, and intelligent recommendations.

## 🌟 Features

### 💬 Conversational AI Advisor
- **Personalized Financial Advice**: AI-powered responses using OpenAI GPT-4o
- **Context-Aware Recommendations**: Advice tailored to your financial profile
- **Real-time Chat Interface**: Interactive financial Q&A experience
- **Risk Assessment Integration**: Advice aligned with your risk tolerance

### 📊 Portfolio Analysis
- **Real-time Portfolio Valuation**: Live market data integration
- **Risk Metrics Calculation**: Volatility, Sharpe ratio, and diversification scoring
- **Performance Tracking**: Historical performance analysis and benchmarking
- **Rebalancing Recommendations**: Intelligent portfolio optimization suggestions

### 🎯 Goal-Based Financial Planning
- **Smart Goal Setting**: Inflation-adjusted financial goal planning
- **Feasibility Assessment**: Realistic timeline and savings requirement analysis
- **Investment Strategy Recommendations**: Goal-appropriate investment approaches
- **Progress Tracking**: Visual progress monitoring with projections

### 📈 Market Insights & Data
- **Real-time Market Data**: Live indices, sector performance, and economic indicators
- **Cryptocurrency Tracking**: Major crypto price monitoring
- **Bond Yield Analysis**: Treasury yield tracking across maturities
- **Market Trend Analysis**: AI-generated market insights and recommendations

### 🤖 ML-Powered Recommendations
- **Collaborative Filtering**: Recommendations based on similar user profiles
- **User Segmentation**: K-means clustering for personalized suggestions
- **Product Database**: Comprehensive investment product recommendations
- **Risk-Appropriate Matching**: Investments aligned with user profiles

### 🛡️ Insurance Advisory
- **Coverage Gap Analysis**: Identify insurance needs and gaps
- **Product Recommendations**: Life, disability, and other insurance suggestions
- **Cost Optimization**: Strategies to reduce insurance costs while maintaining coverage

## 🚀 Quick Start

### Option 1: Replit (Recommended)
1. **Fork this project** on Replit
2. **Add API keys** in the Secrets tab:
   - `OPENAI_API_KEY`: Your OpenAI API key
3. **Run the project** - dependencies install automatically
4. **Access your app** via the provided URL

### Option 2: Local Development
```bash
# Clone the repository
git clone <repository-url>
cd ai-financial-advisory

# Set up Python environment
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install streamlit>=1.46.1 openai>=1.96.0 pandas>=2.3.1 \
           numpy>=2.3.1 plotly>=6.2.0 scikit-learn>=1.7.0 \
           yfinance>=0.2.65 anthropic>=0.57.1

# Set environment variables
export OPENAI_API_KEY="your-openai-key-here"

# Run the application
streamlit run app.py --server.port 5000
```

### API Keys Required
- **OpenAI API Key** (Required): Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Anthropic API Key** (Optional): Get from [Anthropic Console](https://console.anthropic.com/)

## 🏗️ Architecture

### System Overview
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │◄──►│  Business Logic │◄──►│  External APIs  │
│   (Frontend)    │    │     (Utils)     │    │ (OpenAI, Yahoo) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Core Components
- **Financial Advisor**: AI-powered advice generation
- **Portfolio Analyzer**: Investment analysis and risk assessment
- **Goal Planner**: Financial goal setting and tracking
- **Market Data Provider**: Real-time market data integration
- **Recommendation Engine**: ML-based investment recommendations
- **User Profile Manager**: Profile validation and health scoring

### Technology Stack
- **Frontend**: Streamlit with Plotly visualizations
- **AI/ML**: OpenAI GPT-4o, Anthropic Claude, Scikit-learn
- **Data**: Pandas, NumPy, Yahoo Finance API
- **Deployment**: Replit, supports local and cloud deployment

## 📱 Usage Guide

### 1. Profile Setup
- **Create your financial profile** with personal and financial information
- **Set risk tolerance** and investment experience level
- **Define financial goals** (retirement, emergency fund, home purchase, etc.)

### 2. Dashboard Overview
- **View financial health score** with detailed breakdown
- **Monitor key metrics** (savings rate, debt-to-income ratio)
- **Get quick insights** and improvement recommendations

### 3. AI Chat
- **Ask financial questions** in natural language
- **Receive personalized advice** based on your profile
- **Get explanations** for complex financial concepts

### 4. Portfolio Analysis
- **Input your current investments** (stocks, bonds, cash, real estate)
- **View risk assessment** and diversification analysis
- **Get rebalancing recommendations** for optimization

### 5. Goal Planning
- **Set specific financial goals** with target amounts and timelines
- **View monthly savings requirements** and feasibility assessment
- **Get investment strategy recommendations** for each goal

### 6. Market Insights
- **Monitor market performance** across major indices
- **Track sector performance** and identify trends
- **View economic indicators** and their implications

## 🔧 Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY=your-openai-api-key

# Optional
ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Streamlit Configuration
The app includes optimized configuration in `.streamlit/config.toml`:
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
```

## 🧪 Development

### Project Structure
```
ai-financial-advisory/
├── app.py                    # Main application
├── utils/                    # Business logic modules
│   ├── financial_advisor.py      # AI advice generation
│   ├── portfolio_analyzer.py     # Portfolio analysis
│   ├── goal_planner.py          # Financial planning
│   ├── market_data.py           # Market data provider
│   ├── recommendation_engine.py # ML recommendations
│   └── user_profile.py          # User management
├── data/
│   └── mock_users.py            # Test data for ML
├── docs/                     # Comprehensive documentation
│   ├── SETUP.md                 # Setup guide
│   ├── ARCHITECTURE.md          # System architecture
│   ├── API_REFERENCE.md         # API documentation
│   ├── CONTRIBUTING.md          # Contribution guide
│   └── diagrams/               # PlantUML diagrams
└── .streamlit/
    └── config.toml             # Streamlit configuration
```

### Adding Features
1. **Create utility modules** in `utils/` for business logic
2. **Add UI components** in `app.py` using Streamlit
3. **Update documentation** in `docs/` folder
4. **Test thoroughly** with different user profiles

### Code Quality
- **Follow PEP 8** coding standards
- **Add docstrings** to all public functions
- **Handle errors gracefully** with user-friendly messages
- **Use type hints** for better code documentation

## 📊 Key Features Deep Dive

### Financial Health Scoring
- **Savings Rate Analysis**: Compares to recommended 10-20% savings rate
- **Debt-to-Income Assessment**: Evaluates financial burden and risk
- **Emergency Fund Evaluation**: Checks 3-6 month expense coverage
- **Risk Tolerance Alignment**: Age-appropriate investment approach
- **Goal Setting Assessment**: Financial planning completeness

### Machine Learning Recommendations
- **User Segmentation**: K-means clustering based on financial profiles
- **Collaborative Filtering**: Recommendations from similar users
- **Content-Based Filtering**: Product matching based on user preferences
- **Risk-Return Optimization**: Balanced recommendations for user's risk profile

### Real-time Data Integration
- **Market Data**: Yahoo Finance API for stocks, indices, and ETFs
- **Fallback Systems**: Mock data generation when APIs are unavailable
- **Caching Strategy**: Optimized performance with intelligent caching
- **Error Handling**: Graceful degradation with user notifications

## 🔒 Security & Privacy

### Data Protection
- **No Persistent Storage**: User data exists only during session
- **API Key Security**: Environment variable storage, never in code
- **Input Validation**: Comprehensive sanitization of user inputs
- **Session Isolation**: User data never shared between sessions

### Privacy Features
- **Minimal Data Collection**: Only necessary financial parameters
- **No External Tracking**: No third-party analytics or tracking
- **Local Processing**: Most calculations performed locally
- **Transparent Usage**: Clear explanation of data usage

## 🚀 Deployment Options

### Replit (Recommended)
- **One-click deployment** with automatic dependency management
- **Built-in secret management** for API keys
- **Automatic SSL/TLS** with public URL generation
- **Easy sharing** and collaboration features

### Cloud Platforms
- **Heroku**: Simple deployment with Procfile
- **Streamlit Cloud**: Direct integration with GitHub
- **AWS/GCP/Azure**: Enterprise-grade deployment options
- **Docker**: Containerized deployment for any platform

### Local Development
- **Virtual Environment**: Isolated Python environment
- **Environment Variables**: Local `.env` file support
- **Hot Reload**: Streamlit's automatic refresh on code changes
- **Debug Mode**: Enhanced error messages and logging

## 📈 Performance & Scalability

### Current Performance
- **Session-based State**: Fast user experience with memory storage
- **Cached API Calls**: Reduced latency with intelligent caching
- **Optimized Calculations**: Efficient algorithms for financial computations
- **Responsive UI**: Real-time updates with Streamlit's reactive model

### Scaling Considerations
- **Database Integration**: PostgreSQL/MongoDB for persistent storage
- **Multi-user Support**: User authentication and data isolation
- **Microservices**: Component decomposition for large-scale deployment
- **Load Balancing**: Horizontal scaling for high traffic

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/CONTRIBUTING.md) for details on:

- **Code Standards**: Python style guidelines and best practices
- **Development Setup**: Local environment configuration
- **Testing Guidelines**: Unit and integration test requirements
- **Documentation Standards**: Keeping docs current and comprehensive
- **Pull Request Process**: Step-by-step contribution workflow

### Areas for Contribution
- 🚀 **Feature Development**: New analysis tools and integrations
- 🐛 **Bug Fixes**: Performance improvements and error handling
- 📚 **Documentation**: Guides, tutorials, and API documentation
- 🧪 **Testing**: Test coverage expansion and quality assurance
- 🎨 **UI/UX**: Design improvements and accessibility enhancements

## 📚 Documentation

### Complete Documentation Available
- **[Setup Guide](docs/SETUP.md)**: Detailed installation and configuration
- **[Architecture Documentation](docs/ARCHITECTURE.md)**: System design and decisions
- **[API Reference](docs/API_REFERENCE.md)**: Complete API documentation
- **[Contributing Guide](docs/CONTRIBUTING.md)**: Development and contribution guidelines
- **[PlantUML Diagrams](docs/diagrams/)**: Visual system architecture

### Architecture Diagrams
- **System Architecture**: High-level component overview
- **Data Flow**: Request/response flow through the system
- **Component Architecture**: Detailed module interactions
- **Deployment Architecture**: Infrastructure and deployment setup
- **User Journey**: Complete user interaction flow

## 🔄 Recent Updates

### Latest Features
- **Enhanced AI Integration**: OpenAI GPT-4o for superior advice quality
- **Real-time Market Data**: Live integration with Yahoo Finance
- **ML Recommendations**: Collaborative filtering for personalized suggestions
- **Comprehensive Documentation**: Complete setup and development guides
- **PlantUML Diagrams**: Visual architecture documentation

### Upcoming Features
- **Mobile Optimization**: Enhanced mobile user experience
- **Advanced Analytics**: Predictive modeling and forecasting
- **Social Features**: Community recommendations and sharing
- **Multi-language Support**: Internationalization capabilities

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help
- **GitHub Issues**: Bug reports and feature requests
- **Documentation**: Comprehensive guides in `docs/` folder
- **Community**: GitHub Discussions for questions and ideas

### Troubleshooting
- **API Key Issues**: Verify keys are set in environment variables
- **Performance Issues**: Check internet connection and API limits
- **UI Problems**: Clear browser cache and refresh application
- **Installation Issues**: Ensure Python 3.11+ and all dependencies

## 🎯 Project Goals

### Mission Statement
Democratize access to high-quality financial advice through AI technology, making sophisticated financial planning tools available to everyone regardless of their financial background or resources.

### Core Objectives
1. **Accessibility**: Simple, intuitive interface for all experience levels
2. **Personalization**: Tailored advice based on individual financial situations
3. **Education**: Help users understand financial concepts and decisions
4. **Actionability**: Provide specific, implementable recommendations
5. **Security**: Protect user privacy and financial information

---

**Built with ❤️ for democratizing financial advice**

*Empowering individuals to make informed financial decisions through AI-powered guidance and comprehensive analysis tools.*