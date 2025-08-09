import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import streamlit as st

class UserProfile:
    def __init__(self):
        self.required_fields = [
            'name', 'age', 'annual_income', 'employment_status', 
            'risk_tolerance', 'investment_experience', 'monthly_savings'
        ]
        self.optional_fields = [
            'debt_amount', 'financial_goals', 'created_date', 'last_updated'
        ]
        
        # Risk tolerance mapping for scoring
        self.risk_tolerance_scores = {
            'Conservative': 1,
            'Moderate': 2,
            'Aggressive': 3
        }
        
        # Investment experience mapping
        self.experience_scores = {
            'Beginner': 1,
            'Intermediate': 2,
            'Advanced': 3
        }
        
        # Employment status stability scores
        self.employment_stability = {
            'Employed': 3,
            'Self-Employed': 2,
            'Unemployed': 1,
            'Retired': 2,
            'Student': 1
        }
    
    def validate_profile(self, profile_data: Dict) -> Tuple[bool, List[str]]:
        """Validate user profile data and return validation status with error messages"""
        errors = []
        
        # Check required fields
        for field in self.required_fields:
            if field not in profile_data or profile_data[field] is None:
                errors.append(f"Missing required field: {field}")
            elif isinstance(profile_data[field], str) and not profile_data[field].strip():
                errors.append(f"Field '{field}' cannot be empty")
        
        # Validate specific field types and ranges
        if 'age' in profile_data:
            try:
                age = int(profile_data['age'])
                if age < 18 or age > 100:
                    errors.append("Age must be between 18 and 100")
            except (ValueError, TypeError):
                errors.append("Age must be a valid number")
        
        if 'annual_income' in profile_data:
            try:
                income = float(profile_data['annual_income'])
                if income < 0:
                    errors.append("Annual income cannot be negative")
            except (ValueError, TypeError):
                errors.append("Annual income must be a valid number")
        
        if 'monthly_savings' in profile_data:
            try:
                savings = float(profile_data['monthly_savings'])
                if savings < 0:
                    errors.append("Monthly savings cannot be negative")
            except (ValueError, TypeError):
                errors.append("Monthly savings must be a valid number")
        
        if 'debt_amount' in profile_data:
            try:
                debt = float(profile_data['debt_amount'])
                if debt < 0:
                    errors.append("Debt amount cannot be negative")
            except (ValueError, TypeError):
                errors.append("Debt amount must be a valid number")
        
        # Validate enum fields
        if 'risk_tolerance' in profile_data:
            if profile_data['risk_tolerance'] not in self.risk_tolerance_scores:
                errors.append("Risk tolerance must be Conservative, Moderate, or Aggressive")
        
        if 'investment_experience' in profile_data:
            if profile_data['investment_experience'] not in self.experience_scores:
                errors.append("Investment experience must be Beginner, Intermediate, or Advanced")
        
        if 'employment_status' in profile_data:
            if profile_data['employment_status'] not in self.employment_stability:
                errors.append("Employment status must be Employed, Self-Employed, Unemployed, Retired, or Student")
        
        # Logical validation
        if ('annual_income' in profile_data and 'monthly_savings' in profile_data and 
            profile_data['annual_income'] > 0 and profile_data['monthly_savings'] > 0):
            annual_savings = profile_data['monthly_savings'] * 12
            if annual_savings > profile_data['annual_income']:
                errors.append("Monthly savings cannot exceed annual income")
        
        return len(errors) == 0, errors
    
    def create_profile(self, profile_data: Dict) -> Dict:
        """Create a new user profile with validation and default values"""
        # Validate input
        is_valid, errors = self.validate_profile(profile_data)
        if not is_valid:
            raise ValueError(f"Profile validation failed: {', '.join(errors)}")
        
        # Add metadata
        profile = profile_data.copy()
        profile['created_date'] = datetime.now().isoformat()
        profile['last_updated'] = datetime.now().isoformat()
        profile['profile_id'] = self._generate_profile_id(profile_data)
        
        # Set defaults for optional fields
        if 'debt_amount' not in profile:
            profile['debt_amount'] = 0.0
        if 'financial_goals' not in profile:
            profile['financial_goals'] = []
        
        return profile
    
    def update_profile(self, existing_profile: Dict, updates: Dict) -> Dict:
        """Update an existing profile with new data"""
        updated_profile = existing_profile.copy()
        updated_profile.update(updates)
        updated_profile['last_updated'] = datetime.now().isoformat()
        
        # Validate updated profile
        is_valid, errors = self.validate_profile(updated_profile)
        if not is_valid:
            raise ValueError(f"Profile update validation failed: {', '.join(errors)}")
        
        return updated_profile
    
    def _generate_profile_id(self, profile_data: Dict) -> str:
        """Generate a unique profile ID based on user data"""
        # Use name, age, and creation timestamp for uniqueness
        id_string = f"{profile_data.get('name', '')}{profile_data.get('age', '')}{datetime.now().timestamp()}"
        return hashlib.md5(id_string.encode()).hexdigest()[:12]
    
    def calculate_financial_health_score(self, profile: Dict) -> Dict:
        """Calculate a comprehensive financial health score for the user"""
        score_components = {}
        total_score = 0
        max_score = 0
        
        # 1. Savings Rate (25 points max)
        annual_income = profile.get('annual_income', 0)
        monthly_savings = profile.get('monthly_savings', 0)
        
        if annual_income > 0:
            savings_rate = (monthly_savings * 12) / annual_income
            if savings_rate >= 0.20:  # 20%+ is excellent
                savings_score = 25
            elif savings_rate >= 0.15:  # 15-20% is very good
                savings_score = 20
            elif savings_rate >= 0.10:  # 10-15% is good
                savings_score = 15
            elif savings_rate >= 0.05:  # 5-10% is fair
                savings_score = 10
            else:  # <5% is poor
                savings_score = 5
        else:
            savings_score = 0
            savings_rate = 0
        
        score_components['savings_rate'] = {
            'score': savings_score,
            'max_score': 25,
            'percentage': savings_rate * 100,
            'description': f"Savings rate: {savings_rate:.1%}"
        }
        total_score += savings_score
        max_score += 25
        
        # 2. Debt-to-Income Ratio (20 points max)
        debt_amount = profile.get('debt_amount', 0)
        if annual_income > 0:
            debt_to_income = debt_amount / annual_income
            if debt_to_income <= 0.10:  # ≤10% is excellent
                debt_score = 20
            elif debt_to_income <= 0.20:  # 10-20% is good
                debt_score = 15
            elif debt_to_income <= 0.30:  # 20-30% is fair
                debt_score = 10
            elif debt_to_income <= 0.40:  # 30-40% is concerning
                debt_score = 5
            else:  # >40% is poor
                debt_score = 0
        else:
            debt_score = 10  # Neutral if no income data
            debt_to_income = 0
        
        score_components['debt_ratio'] = {
            'score': debt_score,
            'max_score': 20,
            'percentage': debt_to_income * 100,
            'description': f"Debt-to-income ratio: {debt_to_income:.1%}"
        }
        total_score += debt_score
        max_score += 20
        
        # 3. Emergency Fund Adequacy (20 points max)
        monthly_expenses = max(0, (annual_income - monthly_savings * 12) / 12)
        if monthly_expenses > 0:
            emergency_months = monthly_savings / monthly_expenses * 3  # Assuming 3 months of current savings
            if emergency_months >= 6:  # 6+ months is excellent
                emergency_score = 20
            elif emergency_months >= 3:  # 3-6 months is good
                emergency_score = 15
            elif emergency_months >= 1:  # 1-3 months is fair
                emergency_score = 10
            else:  # <1 month is poor
                emergency_score = 5
        else:
            emergency_score = 10  # Neutral if can't calculate
            emergency_months = 0
        
        score_components['emergency_fund'] = {
            'score': emergency_score,
            'max_score': 20,
            'months': emergency_months,
            'description': f"Emergency fund: {emergency_months:.1f} months of expenses"
        }
        total_score += emergency_score
        max_score += 20
        
        # 4. Age-Appropriate Risk Taking (15 points max)
        age = profile.get('age', 30)
        risk_tolerance = profile.get('risk_tolerance', 'Moderate')
        
        # Younger people should generally take more risk
        if age < 30:
            target_risk = 'Aggressive'
        elif age < 50:
            target_risk = 'Moderate'
        else:
            target_risk = 'Conservative'
        
        if risk_tolerance == target_risk:
            risk_score = 15
        elif (age < 30 and risk_tolerance == 'Moderate') or \
             (30 <= age < 50 and risk_tolerance in ['Conservative', 'Aggressive']) or \
             (age >= 50 and risk_tolerance == 'Moderate'):
            risk_score = 10
        else:
            risk_score = 5
        
        score_components['risk_alignment'] = {
            'score': risk_score,
            'max_score': 15,
            'current_risk': risk_tolerance,
            'target_risk': target_risk,
            'description': f"Risk tolerance: {risk_tolerance} (target: {target_risk} for age {age})"
        }
        total_score += risk_score
        max_score += 15
        
        # 5. Financial Goal Setting (10 points max)
        financial_goals = profile.get('financial_goals', [])
        if len(financial_goals) >= 3:
            goals_score = 10
        elif len(financial_goals) >= 2:
            goals_score = 7
        elif len(financial_goals) >= 1:
            goals_score = 5
        else:
            goals_score = 0
        
        score_components['goal_setting'] = {
            'score': goals_score,
            'max_score': 10,
            'num_goals': len(financial_goals),
            'description': f"Financial goals: {len(financial_goals)} defined"
        }
        total_score += goals_score
        max_score += 10
        
        # 6. Employment Stability (10 points max)
        employment_status = profile.get('employment_status', 'Unemployed')
        stability_score = self.employment_stability.get(employment_status, 1) * 3.33  # Scale to 10 points
        stability_score = min(10, stability_score)
        
        score_components['employment_stability'] = {
            'score': stability_score,
            'max_score': 10,
            'status': employment_status,
            'description': f"Employment: {employment_status}"
        }
        total_score += stability_score
        max_score += 10
        
        # Calculate overall score percentage
        overall_percentage = (total_score / max_score) * 100 if max_score > 0 else 0
        
        # Determine overall rating
        if overall_percentage >= 80:
            rating = "Excellent"
            color = "green"
        elif overall_percentage >= 65:
            rating = "Good"
            color = "blue"
        elif overall_percentage >= 50:
            rating = "Fair"
            color = "orange"
        elif overall_percentage >= 35:
            rating = "Needs Improvement"
            color = "red"
        else:
            rating = "Poor"
            color = "darkred"
        
        return {
            'overall_score': round(overall_percentage, 1),
            'rating': rating,
            'color': color,
            'total_points': round(total_score, 1),
            'max_points': max_score,
            'components': score_components,
            'recommendations': self._generate_health_recommendations(score_components, profile)
        }
    
    def _generate_health_recommendations(self, score_components: Dict, profile: Dict) -> List[str]:
        """Generate recommendations based on financial health score components"""
        recommendations = []
        
        # Savings rate recommendations
        savings_component = score_components.get('savings_rate', {})
        if savings_component.get('score', 0) < 15:
            recommendations.append("Increase your savings rate to at least 10-15% of income")
        
        # Debt recommendations
        debt_component = score_components.get('debt_ratio', {})
        if debt_component.get('score', 0) < 10:
            recommendations.append("Focus on reducing high-interest debt to improve financial health")
        
        # Emergency fund recommendations
        emergency_component = score_components.get('emergency_fund', {})
        if emergency_component.get('score', 0) < 15:
            recommendations.append("Build an emergency fund covering 3-6 months of expenses")
        
        # Risk alignment recommendations
        risk_component = score_components.get('risk_alignment', {})
        if risk_component.get('score', 0) < 10:
            current_risk = risk_component.get('current_risk', '')
            target_risk = risk_component.get('target_risk', '')
            recommendations.append(f"Consider adjusting risk tolerance from {current_risk} to {target_risk} for your age")
        
        # Goal setting recommendations
        goals_component = score_components.get('goal_setting', {})
        if goals_component.get('score', 0) < 7:
            recommendations.append("Define specific financial goals to guide your planning")
        
        # Employment stability recommendations
        employment_component = score_components.get('employment_stability', {})
        if employment_component.get('score', 0) < 7:
            recommendations.append("Consider building additional income streams for financial stability")
        
        return recommendations
    
    def get_user_segment(self, profile: Dict) -> str:
        """Categorize user into a segment for targeted recommendations"""
        age = profile.get('age', 30)
        income = profile.get('annual_income', 0)
        risk_tolerance = profile.get('risk_tolerance', 'Moderate')
        experience = profile.get('investment_experience', 'Beginner')
        
        # Young High Earner
        if age < 35 and income > 80000:
            return "Young Professional"
        
        # Conservative Saver
        elif risk_tolerance == 'Conservative' or experience == 'Beginner':
            return "Conservative Saver"
        
        # Aggressive Investor
        elif risk_tolerance == 'Aggressive' and experience in ['Intermediate', 'Advanced']:
            return "Aggressive Investor"
        
        # Pre-Retirement
        elif age >= 50:
            return "Pre-Retirement"
        
        # Family Focused
        elif 'Home Purchase' in profile.get('financial_goals', []) or 'Education' in profile.get('financial_goals', []):
            return "Family Focused"
        
        # Default to Balanced Investor
        else:
            return "Balanced Investor"
    
    def compare_profiles(self, profile1: Dict, profile2: Dict) -> Dict:
        """Compare two user profiles and highlight differences"""
        comparison = {
            'similarities': [],
            'differences': [],
            'recommendations': []
        }
        
        # Compare key metrics
        age_diff = abs(profile1.get('age', 0) - profile2.get('age', 0))
        if age_diff <= 5:
            comparison['similarities'].append(f"Similar age group (within {age_diff} years)")
        else:
            comparison['differences'].append(f"Different age groups ({age_diff} years apart)")
        
        income_diff = abs(profile1.get('annual_income', 0) - profile2.get('annual_income', 0))
        income_pct_diff = income_diff / max(profile1.get('annual_income', 1), profile2.get('annual_income', 1)) * 100
        
        if income_pct_diff <= 20:
            comparison['similarities'].append("Similar income levels")
        else:
            comparison['differences'].append(f"Different income levels ({income_pct_diff:.0f}% difference)")
        
        # Risk tolerance comparison
        if profile1.get('risk_tolerance') == profile2.get('risk_tolerance'):
            comparison['similarities'].append("Same risk tolerance")
        else:
            comparison['differences'].append("Different risk tolerance levels")
        
        # Generate recommendations based on comparison
        if len(comparison['similarities']) > len(comparison['differences']):
            comparison['recommendations'].append("These profiles are quite similar - collaborative recommendations would be effective")
        else:
            comparison['recommendations'].append("These profiles have significant differences - personalized recommendations are more appropriate")
        
        return comparison
    
    def export_profile(self, profile: Dict, format: str = 'json') -> str:
        """Export user profile in specified format"""
        if format.lower() == 'json':
            return json.dumps(profile, indent=2, default=str)
        elif format.lower() == 'summary':
            return self._generate_profile_summary(profile)
        else:
            raise ValueError("Unsupported export format. Use 'json' or 'summary'")
    
    def _generate_profile_summary(self, profile: Dict) -> str:
        """Generate a human-readable profile summary"""
        summary = f"""
Financial Profile Summary
========================

Personal Information:
- Name: {profile.get('name', 'N/A')}
- Age: {profile.get('age', 'N/A')}
- Employment: {profile.get('employment_status', 'N/A')}

Financial Details:
- Annual Income: ${profile.get('annual_income', 0):,}
- Monthly Savings: ${profile.get('monthly_savings', 0):,}
- Total Debt: ${profile.get('debt_amount', 0):,}
- Savings Rate: {(profile.get('monthly_savings', 0) * 12 / max(profile.get('annual_income', 1), 1) * 100):.1f}%

Investment Profile:
- Risk Tolerance: {profile.get('risk_tolerance', 'N/A')}
- Investment Experience: {profile.get('investment_experience', 'N/A')}

Financial Goals:
{chr(10).join([f"- {goal}" for goal in profile.get('financial_goals', ['No goals defined'])])}

Profile Created: {profile.get('created_date', 'N/A')}
Last Updated: {profile.get('last_updated', 'N/A')}
"""
        return summary.strip()
    
    def get_profile_analytics(self, profiles: List[Dict]) -> Dict:
        """Generate analytics across multiple user profiles"""
        if not profiles:
            return {'error': 'No profiles provided'}
        
        analytics = {
            'total_users': len(profiles),
            'demographics': {},
            'financial_metrics': {},
            'risk_distribution': {},
            'goal_analysis': {}
        }
        
        # Demographics
        ages = [p.get('age', 0) for p in profiles if p.get('age')]
        if ages:
            analytics['demographics'] = {
                'avg_age': round(sum(ages) / len(ages), 1),
                'age_range': f"{min(ages)}-{max(ages)}",
                'median_age': sorted(ages)[len(ages)//2]
            }
        
        # Financial metrics
        incomes = [p.get('annual_income', 0) for p in profiles if p.get('annual_income')]
        savings = [p.get('monthly_savings', 0) for p in profiles if p.get('monthly_savings')]
        
        if incomes:
            analytics['financial_metrics'] = {
                'avg_income': round(sum(incomes) / len(incomes), 0),
                'median_income': sorted(incomes)[len(incomes)//2],
                'income_range': f"${min(incomes):,} - ${max(incomes):,}"
            }
        
        if savings:
            analytics['financial_metrics']['avg_monthly_savings'] = round(sum(savings) / len(savings), 0)
        
        # Risk distribution
        risk_counts = {}
        for profile in profiles:
            risk = profile.get('risk_tolerance', 'Unknown')
            risk_counts[risk] = risk_counts.get(risk, 0) + 1
        
        analytics['risk_distribution'] = {
            risk: f"{count} ({count/len(profiles)*100:.1f}%)" 
            for risk, count in risk_counts.items()
        }
        
        # Goal analysis
        all_goals = []
        for profile in profiles:
            all_goals.extend(profile.get('financial_goals', []))
        
        goal_counts = {}
        for goal in all_goals:
            goal_counts[goal] = goal_counts.get(goal, 0) + 1
        
        analytics['goal_analysis'] = dict(sorted(goal_counts.items(), key=lambda x: x[1], reverse=True)[:5])
        
        return analytics
