import os
import json
from openai import OpenAI

class FinancialAdvisor:
    def __init__(self):
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "default_key"))
        self.model = "gpt-4o"
    
    def get_personalized_advice(self, user_query, user_profile):
        """Generate personalized financial advice based on user query and profile"""
        
        # Create context from user profile
        profile_context = f"""
        User Profile:
        - Name: {user_profile.get('name', 'User')}
        - Age: {user_profile.get('age')}
        - Annual Income: ${user_profile.get('annual_income', 0):,}
        - Employment: {user_profile.get('employment_status')}
        - Risk Tolerance: {user_profile.get('risk_tolerance')}
        - Investment Experience: {user_profile.get('investment_experience')}
        - Monthly Savings: ${user_profile.get('monthly_savings', 0):,}
        - Total Debt: ${user_profile.get('debt_amount', 0):,}
        - Financial Goals: {', '.join(user_profile.get('financial_goals', []))}
        """
        
        system_prompt = """You are a professional financial advisor AI. Provide personalized, actionable financial advice based on the user's profile and query. 

Guidelines:
- Be specific and actionable in your recommendations
- Consider the user's risk tolerance, age, and financial situation
- Provide educational explanations for your recommendations
- Always include appropriate disclaimers
- Focus on practical steps the user can take
- Be encouraging but realistic
- If the query is about investments, consider diversification and risk management

Always start responses with a brief acknowledgment of their question and end with a disclaimer about seeking professional advice for major financial decisions."""
        
        try:
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{profile_context}\n\nUser Question: {user_query}"}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your request right now. Error: {str(e)}. Please try again or rephrase your question."
    
    def get_quick_insights(self, user_profile):
        """Generate quick financial insights based on user profile"""
        insights = []
        
        # Savings rate analysis
        annual_savings = user_profile.get('monthly_savings', 0) * 12
        savings_rate = (annual_savings / user_profile.get('annual_income', 1)) * 100
        
        if savings_rate < 10:
            insights.append(f"💡 Your current savings rate is {savings_rate:.1f}%. Consider aiming for at least 10-15% of your income.")
        elif savings_rate < 20:
            insights.append(f"✅ Good job! Your savings rate of {savings_rate:.1f}% is on track. Consider increasing to 20% if possible.")
        else:
            insights.append(f"🌟 Excellent! Your savings rate of {savings_rate:.1f}% puts you ahead of most people.")
        
        # Debt-to-income ratio
        debt_to_income = (user_profile.get('debt_amount', 0) / user_profile.get('annual_income', 1)) * 100
        if debt_to_income > 40:
            insights.append(f"⚠️ Your debt-to-income ratio is {debt_to_income:.1f}%. Focus on debt reduction as a priority.")
        elif debt_to_income > 20:
            insights.append(f"📊 Your debt-to-income ratio is {debt_to_income:.1f}%. Consider a debt reduction strategy.")
        else:
            insights.append(f"✅ Your debt levels are manageable at {debt_to_income:.1f}% of income.")
        
        # Emergency fund calculation
        monthly_expenses = user_profile.get('annual_income', 0) / 12 - user_profile.get('monthly_savings', 0)
        emergency_fund_months = user_profile.get('monthly_savings', 0) * 3 / monthly_expenses if monthly_expenses > 0 else 0
        
        if emergency_fund_months < 3:
            insights.append("🚨 Build an emergency fund covering 3-6 months of expenses as your first priority.")
        elif emergency_fund_months < 6:
            insights.append("💪 You're building a good emergency fund. Aim for 6 months of expenses.")
        
        # Age-based insights
        age = user_profile.get('age', 30)
        if age < 30:
            insights.append("🚀 You have time on your side! Focus on aggressive growth investments and building good financial habits.")
        elif age < 50:
            insights.append("⚖️ Balance growth and stability in your investment approach as you advance in your career.")
        else:
            insights.append("🎯 Focus on capital preservation and income generation as you approach or enter retirement.")
        
        return insights
    
    def get_risk_assessment(self, user_profile):
        """Assess user's financial risk profile"""
        risk_factors = {
            'age': user_profile.get('age', 30),
            'income': user_profile.get('annual_income', 0),
            'debt': user_profile.get('debt_amount', 0),
            'savings_rate': (user_profile.get('monthly_savings', 0) * 12) / max(user_profile.get('annual_income', 1), 1),
            'risk_tolerance': user_profile.get('risk_tolerance', 'Moderate'),
            'experience': user_profile.get('investment_experience', 'Beginner')
        }
        
        # Calculate risk score (1-10 scale)
        risk_score = 5  # baseline
        
        # Age factor (younger = higher risk capacity)
        if risk_factors['age'] < 30:
            risk_score += 2
        elif risk_factors['age'] < 50:
            risk_score += 1
        else:
            risk_score -= 1
        
        # Income stability
        if risk_factors['income'] > 100000:
            risk_score += 1
        elif risk_factors['income'] < 40000:
            risk_score -= 1
        
        # Debt burden
        debt_ratio = risk_factors['debt'] / max(risk_factors['income'], 1)
        if debt_ratio > 0.4:
            risk_score -= 2
        elif debt_ratio > 0.2:
            risk_score -= 1
        
        # Savings rate
        if risk_factors['savings_rate'] > 0.2:
            risk_score += 1
        elif risk_factors['savings_rate'] < 0.1:
            risk_score -= 1
        
        # Risk tolerance
        tolerance_map = {'Conservative': -1, 'Moderate': 0, 'Aggressive': 2}
        risk_score += tolerance_map.get(risk_factors['risk_tolerance'], 0)
        
        # Experience
        experience_map = {'Beginner': -1, 'Intermediate': 0, 'Advanced': 1}
        risk_score += experience_map.get(risk_factors['experience'], 0)
        
        # Clamp between 1-10
        risk_score = max(1, min(10, risk_score))
        
        return {
            'risk_score': risk_score,
            'risk_factors': risk_factors,
            'recommendation': self._get_risk_recommendation(risk_score)
        }
    
    def _get_risk_recommendation(self, risk_score):
        """Get investment recommendation based on risk score"""
        if risk_score <= 3:
            return "Conservative portfolio: Focus on bonds, CDs, and stable value funds. Minimal stock exposure."
        elif risk_score <= 5:
            return "Moderate portfolio: Balanced mix of stocks and bonds (60/40 or 70/30). Diversified approach."
        elif risk_score <= 7:
            return "Growth-oriented portfolio: Higher stock allocation (80/20). Focus on diversified equity funds."
        else:
            return "Aggressive portfolio: Primarily stocks with growth focus. Consider individual stocks and growth funds."
