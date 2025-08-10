import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Import utility modules
from utils.financial_advisor import FinancialAdvisor
from utils.portfolio_analyzer import PortfolioAnalyzer
from utils.goal_planner import GoalPlanner
from utils.market_data import MarketDataProvider
from utils.recommendation_engine import RecommendationEngine
from utils.user_profile import UserProfile

# Page configuration
st.set_page_config(
    page_title="AI Financial Advisory Platform",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'portfolio_data' not in st.session_state:
    st.session_state.portfolio_data = None

# Initialize components
@st.cache_resource
def initialize_components():
    advisor = FinancialAdvisor()
    portfolio_analyzer = PortfolioAnalyzer()
    goal_planner = GoalPlanner()
    market_data = MarketDataProvider()
    recommendation_engine = RecommendationEngine()
    user_profile = UserProfile()
    return advisor, portfolio_analyzer, goal_planner, market_data, recommendation_engine, user_profile

advisor, portfolio_analyzer, goal_planner, market_data, recommendation_engine, user_profile = initialize_components()

# Sidebar navigation
st.sidebar.title("🏦 AI Financial Advisory")
st.sidebar.markdown("---")

# User profile section in sidebar
if st.session_state.user_profile is None:
    st.sidebar.subheader("👤 Create Your Profile")
    if st.sidebar.button("Setup Profile"):
        st.session_state.current_page = "profile_setup"
else:
    st.sidebar.subheader("👤 Your Profile")
    profile = st.session_state.user_profile
    st.sidebar.write(f"**Name:** {profile.get('name', 'User')}")
    st.sidebar.write(f"**Age:** {profile.get('age', 'N/A')}")
    st.sidebar.write(f"**Risk Tolerance:** {profile.get('risk_tolerance', 'N/A')}")
    st.sidebar.write(f"**Income:** ${profile.get('annual_income', 0):,}")
    if st.sidebar.button("Edit Profile"):
        st.session_state.current_page = "profile_setup"

st.sidebar.markdown("---")

# Navigation
page = st.sidebar.selectbox(
    "Navigate to:",
    ["🏠 Dashboard", "💬 AI Chat", "📊 Portfolio Analysis", "🎯 Goal Planning", "📈 Market Insights", "🛡️ Insurance Advisory"]
)

# Main content based on selected page
if 'current_page' in st.session_state and st.session_state.current_page == "profile_setup":
    st.title("👤 Setup Your Financial Profile")
    
    with st.form("user_profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", value=st.session_state.user_profile.get('name', '') if st.session_state.user_profile else '')
            age = st.number_input("Age", min_value=18, max_value=100, value=st.session_state.user_profile.get('age', 30) if st.session_state.user_profile else 30)
            annual_income = st.number_input("Annual Income ($)", min_value=0, value=st.session_state.user_profile.get('annual_income', 50000) if st.session_state.user_profile else 50000)
            employment_status = st.selectbox("Employment Status", 
                                           ["Employed", "Self-Employed", "Unemployed", "Retired", "Student"],
                                           index=0 if not st.session_state.user_profile else ["Employed", "Self-Employed", "Unemployed", "Retired", "Student"].index(st.session_state.user_profile.get('employment_status', 'Employed')))
        
        with col2:
            risk_tolerance = st.selectbox("Risk Tolerance", 
                                        ["Conservative", "Moderate", "Aggressive"],
                                        index=1 if not st.session_state.user_profile else ["Conservative", "Moderate", "Aggressive"].index(st.session_state.user_profile.get('risk_tolerance', 'Moderate')))
            investment_experience = st.selectbox("Investment Experience",
                                                ["Beginner", "Intermediate", "Advanced"],
                                                index=0 if not st.session_state.user_profile else ["Beginner", "Intermediate", "Advanced"].index(st.session_state.user_profile.get('investment_experience', 'Beginner')))
            monthly_savings = st.number_input("Monthly Savings ($)", min_value=0, value=st.session_state.user_profile.get('monthly_savings', 500) if st.session_state.user_profile else 500)
            debt_amount = st.number_input("Total Debt ($)", min_value=0, value=st.session_state.user_profile.get('debt_amount', 0) if st.session_state.user_profile else 0)
        
        financial_goals = st.multiselect("Primary Financial Goals",
                                       ["Retirement Planning", "Emergency Fund", "Home Purchase", "Education", "Investment Growth", "Debt Reduction"],
                                       default=st.session_state.user_profile.get('financial_goals', []) if st.session_state.user_profile else [])
        
        if st.form_submit_button("Save Profile"):
            profile_data = {
                'name': name,
                'age': age,
                'annual_income': annual_income,
                'employment_status': employment_status,
                'risk_tolerance': risk_tolerance,
                'investment_experience': investment_experience,
                'monthly_savings': monthly_savings,
                'debt_amount': debt_amount,
                'financial_goals': financial_goals,
                'created_date': datetime.now().isoformat()
            }
            st.session_state.user_profile = profile_data
            st.success("Profile saved successfully!")
            del st.session_state.current_page
            st.rerun()

elif page == "🏠 Dashboard":
    st.title("🏠 Financial Dashboard")
    
    if st.session_state.user_profile is None:
        st.warning("Please create your profile first to access personalized features.")
        st.stop()
    
    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Annual Income", f"${st.session_state.user_profile['annual_income']:,}")
    with col2:
        st.metric("Monthly Savings", f"${st.session_state.user_profile['monthly_savings']:,}")
    with col3:
        savings_rate = (st.session_state.user_profile['monthly_savings'] * 12) / st.session_state.user_profile['annual_income'] * 100
        st.metric("Savings Rate", f"{savings_rate:.1f}%")
    with col4:
        st.metric("Total Debt", f"${st.session_state.user_profile['debt_amount']:,}")
    
    # Quick insights
    st.subheader("📊 Quick Insights")
    insights = advisor.get_quick_insights(st.session_state.user_profile)
    for insight in insights:
        st.info(insight)
    
    # Market overview
    st.subheader("📈 Market Overview")
    market_overview = market_data.get_market_overview()
    
    col1, col2 = st.columns(2)
    with col1:
        # Market indices chart
        fig = go.Figure()
        for index, data in market_overview.items():
            fig.add_trace(go.Scatter(
                x=list(range(len(data['prices']))),
                y=data['prices'],
                mode='lines',
                name=index,
                line=dict(width=2)
            ))
        fig.update_layout(
            title="Market Indices Performance (Last 30 Days)",
            xaxis_title="Days",
            yaxis_title="Price",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Market summary
        st.write("**Market Summary:**")
        for index, data in market_overview.items():
            change = data['change']
            color = "🟢" if change >= 0 else "🔴"
            st.write(f"{color} **{index}**: {data['current_price']:.2f} ({change:+.2f}%)")

elif page == "💬 AI Chat":
    st.title("💬 AI Financial Advisor Chat")
    
    if st.session_state.user_profile is None:
        st.warning("Please create your profile first to access personalized advice.")
        st.stop()
    
    # Disclaimer
    st.warning("⚠️ **Disclaimer**: This AI provides general financial information and should not be considered as professional financial advice. Always consult with a qualified financial advisor for personalized recommendations.")
    
    # Chat interface
    chat_container = st.container()
    
    # Display chat history
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.write(f"**You:** {message['content']}")
            else:
                st.write(f"**AI Advisor:** {message['content']}")
    
    # Chat input
    user_input = st.text_input("Ask me anything about your finances:", key="chat_input")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        send_button = st.button("Send")
    with col2:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    if send_button and user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get AI response
        with st.spinner("AI is thinking..."):
            response = advisor.get_personalized_advice(user_input, st.session_state.user_profile)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        st.rerun()

elif page == "📊 Portfolio Analysis":
    st.title("📊 Portfolio Analysis")
    
    if st.session_state.user_profile is None:
        st.warning("Please create your profile first to access portfolio analysis.")
        st.stop()
    
    # Portfolio input
    st.subheader("Enter Your Current Portfolio")
    
    with st.form("portfolio_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Stocks/ETFs:**")
            stocks_input = st.text_area("Enter symbols and amounts (e.g., AAPL:1000, GOOGL:2000)", 
                                       help="Format: SYMBOL:AMOUNT, one per line or comma-separated")
        
        with col2:
            st.write("**Other Investments:**")
            bonds_amount = st.number_input("Bonds ($)", min_value=0.0, value=0.0)
            cash_amount = st.number_input("Cash ($)", min_value=0.0, value=0.0)
            real_estate_amount = st.number_input("Real Estate ($)", min_value=0.0, value=0.0)
            crypto_amount = st.number_input("Cryptocurrency ($)", min_value=0.0, value=0.0)
        
        if st.form_submit_button("Analyze Portfolio"):
            # Parse stocks input
            portfolio_data = {
                'stocks': {},
                'bonds': bonds_amount,
                'cash': cash_amount,
                'real_estate': real_estate_amount,
                'crypto': crypto_amount
            }
            
            if stocks_input:
                try:
                    for line in stocks_input.replace(',', '\n').split('\n'):
                        line = line.strip()
                        if ':' in line:
                            symbol, amount = line.split(':')
                            portfolio_data['stocks'][symbol.strip().upper()] = float(amount.strip())
                except Exception as e:
                    st.error(f"Error parsing stocks input: {e}")
                    st.stop()
            
            st.session_state.portfolio_data = portfolio_data
    
    # Portfolio analysis
    if st.session_state.portfolio_data:
        analysis = portfolio_analyzer.analyze_portfolio(st.session_state.portfolio_data, st.session_state.user_profile)
        
        # Portfolio composition
        st.subheader("Portfolio Composition")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart of allocation
            labels = []
            values = []
            
            for stock, amount in st.session_state.portfolio_data['stocks'].items():
                labels.append(stock)
                values.append(amount)
            
            if st.session_state.portfolio_data['bonds'] > 0:
                labels.append('Bonds')
                values.append(st.session_state.portfolio_data['bonds'])
            if st.session_state.portfolio_data['cash'] > 0:
                labels.append('Cash')
                values.append(st.session_state.portfolio_data['cash'])
            if st.session_state.portfolio_data['real_estate'] > 0:
                labels.append('Real Estate')
                values.append(st.session_state.portfolio_data['real_estate'])
            if st.session_state.portfolio_data['crypto'] > 0:
                labels.append('Crypto')
                values.append(st.session_state.portfolio_data['crypto'])
            
            if labels and values:
                fig = px.pie(values=values, names=labels, title="Portfolio Allocation")
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.write("**Portfolio Metrics:**")
            st.write(f"Total Value: ${analysis['total_value']:,.2f}")
            st.write(f"Risk Score: {analysis['risk_score']:.2f}/10")
            st.write(f"Diversification Score: {analysis['diversification_score']:.2f}/10")
            
            st.write("**Risk Assessment:**")
            st.write(analysis['risk_assessment'])
        
        # Recommendations
        st.subheader("📝 Recommendations")
        for recommendation in analysis['recommendations']:
            st.write(f"• {recommendation}")
        
        # Performance tracking
        if st.session_state.portfolio_data['stocks']:
            st.subheader("📈 Stock Performance")
            performance_data = portfolio_analyzer.get_stock_performance(list(st.session_state.portfolio_data['stocks'].keys()))
            
            if performance_data:
                df = pd.DataFrame(performance_data)
                fig = px.line(df, x='date', y='close', color='symbol', title="Stock Price Performance (30 Days)")
                st.plotly_chart(fig, use_container_width=True)

elif page == "🎯 Goal Planning":
    st.title("🎯 Goal-Based Financial Planning")
    
    if st.session_state.user_profile is None:
        st.warning("Please create your profile first to access goal planning.")
        st.stop()
    
    # Goal setup
    st.subheader("Set Your Financial Goals")
    
    with st.form("goal_form"):
        goal_name = st.text_input("Goal Name (e.g., 'Emergency Fund', 'House Down Payment')")
        goal_amount = st.number_input("Target Amount ($)", min_value=0.0, value=10000.0)
        goal_timeline = st.number_input("Timeline (years)", min_value=0.1, value=5.0, step=0.1)
        goal_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        
        if st.form_submit_button("Add Goal"):
            if goal_name:
                goal_plan = goal_planner.create_goal_plan(
                    goal_name, goal_amount, goal_timeline, goal_priority, st.session_state.user_profile
                )
                
                st.success(f"Goal '{goal_name}' added successfully!")
                
                # Display goal plan
                st.subheader(f"Plan for: {goal_name}")
                st.write(f"**Target Amount:** ${goal_amount:,.2f}")
                st.write(f"**Timeline:** {goal_timeline} years")
                st.write(f"**Monthly Savings Needed:** ${goal_plan['monthly_savings_needed']:.2f}")
                st.write(f"**Feasibility:** {goal_plan['feasibility']}")
                
                # Progress visualization
                months = int(goal_timeline * 12)
                monthly_savings = goal_plan['monthly_savings_needed']
                
                # Create projection chart
                projection_data = []
                current_amount = 0
                for month in range(months + 1):
                    projection_data.append({
                        'month': month,
                        'amount': current_amount,
                        'target': goal_amount
                    })
                    current_amount += monthly_savings
                
                df = pd.DataFrame(projection_data)
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df['month'], y=df['amount'], mode='lines', name='Projected Savings', line=dict(color='blue')))
                fig.add_trace(go.Scatter(x=df['month'], y=df['target'], mode='lines', name='Target Amount', line=dict(color='red', dash='dash')))
                fig.update_layout(title=f"Savings Projection for {goal_name}", xaxis_title="Months", yaxis_title="Amount ($)")
                st.plotly_chart(fig, use_container_width=True)
                
                # Recommendations
                st.subheader("📝 Recommendations")
                for rec in goal_plan['recommendations']:
                    st.write(f"• {rec}")

elif page == "📈 Market Insights":
    st.title("📈 Market Insights & Analysis")
    
    # Market data
    market_data_provider = market_data
    insights = market_data_provider.get_market_insights()
    
    # Market indices performance
    st.subheader("Market Indices Performance")
    market_overview = market_data_provider.get_market_overview()
    
    # Create performance chart
    fig = go.Figure()
    for index, data in market_overview.items():
        fig.add_trace(go.Scatter(
            x=list(range(len(data['prices']))),
            y=data['prices'],
            mode='lines',
            name=index,
            line=dict(width=2)
        ))
    
    fig.update_layout(
        title="Market Indices Performance (Last 30 Days)",
        xaxis_title="Days",
        yaxis_title="Price",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Market insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Market Summary")
        for index, data in market_overview.items():
            change = data['change']
            color = "green" if change >= 0 else "red"
            st.markdown(f"**{index}**: {data['current_price']:.2f} <span style='color:{color}'>({change:+.2f}%)</span>", unsafe_allow_html=True)
    
    with col2:
        st.subheader("🔍 Market Insights")
        for insight in insights:
            st.info(insight)
    
    # Sector analysis
    st.subheader("📊 Sector Analysis")
    sector_data = market_data_provider.get_sector_performance()
    
    if sector_data:
        df = pd.DataFrame(list(sector_data.items()), columns=['Sector', 'Performance'])
        fig = px.bar(df, x='Sector', y='Performance', title="Sector Performance (%)")
        fig.update_xaxis(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

elif page == "🛡️ Insurance Advisory":
    st.title("🛡️ Insurance Advisory")
    
    if st.session_state.user_profile is None:
        st.warning("Please create your profile first to access insurance recommendations.")
        st.stop()
    
    # Insurance needs analysis
    st.subheader("Insurance Needs Analysis")
    
    profile = st.session_state.user_profile
    
    # Basic insurance calculations
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Life Insurance Recommendation:**")
        life_insurance_need = profile['annual_income'] * 10 + profile['debt_amount']
        st.write(f"Recommended Coverage: ${life_insurance_need:,.2f}")
        st.write("*Based on 10x annual income plus debt coverage*")
        
        st.write("**Disability Insurance:**")
        disability_coverage = profile['annual_income'] * 0.6
        st.write(f"Recommended Coverage: ${disability_coverage:,.2f}/year")
        st.write("*60% of annual income replacement*")
    
    with col2:
        st.write("**Health Insurance:**")
        if profile['employment_status'] == 'Employed':
            st.write("✅ Likely covered through employer")
            st.write("Consider supplemental coverage if needed")
        else:
            st.write("❗ Individual health insurance recommended")
        
        st.write("**Property Insurance:**")
        if 'Home Purchase' in profile.get('financial_goals', []):
            st.write("🏠 Homeowners insurance will be required")
        else:
            st.write("🏠 Renters insurance recommended")
    
    # Insurance recommendations based on profile
    st.subheader("📋 Personalized Insurance Recommendations")
    
    recommendations = []
    
    # Age-based recommendations
    if profile['age'] < 30:
        recommendations.append("Term life insurance is most cost-effective at your age")
        recommendations.append("Consider disability insurance to protect future earnings")
    elif profile['age'] < 50:
        recommendations.append("Review life insurance needs as family situation changes")
        recommendations.append("Consider long-term care insurance planning")
    else:
        recommendations.append("Evaluate permanent life insurance for estate planning")
        recommendations.append("Long-term care insurance becomes more important")
    
    # Income-based recommendations
    if profile['annual_income'] > 100000:
        recommendations.append("Consider umbrella liability insurance for asset protection")
        recommendations.append("Higher disability insurance coverage recommended")
    
    # Goal-based recommendations
    if 'Retirement Planning' in profile.get('financial_goals', []):
        recommendations.append("Consider life insurance as part of retirement strategy")
    
    if profile['debt_amount'] > 0:
        recommendations.append("Ensure life insurance covers outstanding debts")
    
    for rec in recommendations:
        st.write(f"• {rec}")
    
    # Insurance cost estimation
    st.subheader("💰 Estimated Insurance Costs")
    
    # Simple cost estimation based on age and income
    age = profile['age']
    income = profile['annual_income']
    
    # Term life insurance (rough estimate: $1-2 per $1000 coverage per month)
    term_life_monthly = (life_insurance_need / 1000) * 1.5
    
    # Disability insurance (roughly 1-3% of income)
    disability_monthly = income * 0.02 / 12
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Est. Term Life Insurance", f"${term_life_monthly:.0f}/month")
    with col2:
        st.metric("Est. Disability Insurance", f"${disability_monthly:.0f}/month")
    
    st.write("*These are rough estimates. Actual costs vary based on health, lifestyle, and specific coverage needs.*")

# Footer
st.markdown("---")
st.markdown("**Disclaimer**: This platform provides general financial information and educational content. It does not constitute professional financial advice. Always consult with qualified financial advisors before making investment decisions.")
