import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class RecommendationEngine:
    def __init__(self):
        self.user_clusters = None
        self.scaler = StandardScaler()
        self.is_fitted = False
        
        # Investment products database
        self.investment_products = {
            'Conservative': [
                {
                    'name': 'Vanguard Total Bond Market ETF (BND)',
                    'type': 'Bond ETF',
                    'risk_level': 'Low',
                    'expense_ratio': 0.03,
                    'description': 'Broad exposure to U.S. investment-grade bonds',
                    'min_investment': 1,
                    'liquidity': 'High'
                },
                {
                    'name': 'High-Yield Savings Account',
                    'type': 'Cash Equivalent',
                    'risk_level': 'Very Low',
                    'expense_ratio': 0.0,
                    'description': 'FDIC insured savings with competitive interest rates',
                    'min_investment': 1,
                    'liquidity': 'Very High'
                },
                {
                    'name': 'Treasury Inflation-Protected Securities (TIPS)',
                    'type': 'Government Bond',
                    'risk_level': 'Low',
                    'expense_ratio': 0.0,
                    'description': 'Government bonds that adjust for inflation',
                    'min_investment': 100,
                    'liquidity': 'High'
                }
            ],
            'Moderate': [
                {
                    'name': 'Vanguard Target Retirement Fund',
                    'type': 'Target Date Fund',
                    'risk_level': 'Moderate',
                    'expense_ratio': 0.15,
                    'description': 'Age-appropriate asset allocation that adjusts over time',
                    'min_investment': 1000,
                    'liquidity': 'High'
                },
                {
                    'name': 'Vanguard Total Stock Market ETF (VTI)',
                    'type': 'Stock ETF',
                    'risk_level': 'Moderate-High',
                    'expense_ratio': 0.03,
                    'description': 'Complete exposure to U.S. stock market',
                    'min_investment': 1,
                    'liquidity': 'High'
                },
                {
                    'name': 'iShares Core S&P 500 ETF (IVV)',
                    'type': 'Stock ETF',
                    'risk_level': 'Moderate-High',
                    'expense_ratio': 0.03,
                    'description': 'Tracks the S&P 500 index',
                    'min_investment': 1,
                    'liquidity': 'High'
                }
            ],
            'Aggressive': [
                {
                    'name': 'Vanguard Growth ETF (VUG)',
                    'type': 'Growth Stock ETF',
                    'risk_level': 'High',
                    'expense_ratio': 0.04,
                    'description': 'Large-cap growth stocks with high growth potential',
                    'min_investment': 1,
                    'liquidity': 'High'
                },
                {
                    'name': 'Vanguard Small-Cap ETF (VB)',
                    'type': 'Small-Cap ETF',
                    'risk_level': 'High',
                    'expense_ratio': 0.05,
                    'description': 'Small-capitalization U.S. stocks',
                    'min_investment': 1,
                    'liquidity': 'High'
                },
                {
                    'name': 'Vanguard Emerging Markets ETF (VWO)',
                    'type': 'International ETF',
                    'risk_level': 'High',
                    'expense_ratio': 0.10,
                    'description': 'Exposure to emerging market economies',
                    'min_investment': 1,
                    'liquidity': 'High'
                }
            ]
        }
        
        # Insurance products
        self.insurance_products = {
            'Life Insurance': [
                {
                    'name': 'Term Life Insurance',
                    'type': 'Term Life',
                    'coverage_period': '10-30 years',
                    'description': 'Temporary coverage with lower premiums',
                    'best_for': 'Young families with temporary needs'
                },
                {
                    'name': 'Whole Life Insurance',
                    'type': 'Permanent Life',
                    'coverage_period': 'Lifetime',
                    'description': 'Permanent coverage with cash value component',
                    'best_for': 'Estate planning and long-term wealth transfer'
                }
            ],
            'Disability Insurance': [
                {
                    'name': 'Short-Term Disability',
                    'type': 'Disability',
                    'coverage_period': '3-12 months',
                    'description': 'Covers temporary inability to work',
                    'best_for': 'Income protection during recovery'
                },
                {
                    'name': 'Long-Term Disability',
                    'type': 'Disability',
                    'coverage_period': 'Until retirement',
                    'description': 'Covers extended inability to work',
                    'best_for': 'Long-term income protection'
                }
            ]
        }
    
    def get_personalized_recommendations(self, user_profile, recommendation_type='investment'):
        """Get personalized recommendations based on user profile"""
        
        if recommendation_type == 'investment':
            return self._get_investment_recommendations(user_profile)
        elif recommendation_type == 'insurance':
            return self._get_insurance_recommendations(user_profile)
        else:
            return self._get_comprehensive_recommendations(user_profile)
    
    def _get_investment_recommendations(self, user_profile):
        """Generate investment recommendations based on user profile"""
        
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        age = user_profile.get('age', 30)
        income = user_profile.get('annual_income', 50000)
        experience = user_profile.get('investment_experience', 'Beginner')
        goals = user_profile.get('financial_goals', [])
        
        recommendations = []
        
        # Get base recommendations by risk tolerance
        base_products = self.investment_products.get(risk_tolerance, self.investment_products['Moderate'])
        
        # Score and rank products
        scored_products = []
        for product in base_products:
            score = self._calculate_product_score(product, user_profile)
            scored_products.append((product, score))
        
        # Sort by score
        scored_products.sort(key=lambda x: x[1], reverse=True)
        
        # Generate top recommendations
        for product, score in scored_products[:3]:
            recommendation = {
                'product': product,
                'score': score,
                'reasoning': self._generate_product_reasoning(product, user_profile),
                'allocation_suggestion': self._suggest_allocation(product, user_profile)
            }
            recommendations.append(recommendation)
        
        # Add goal-specific recommendations
        goal_recommendations = self._get_goal_specific_recommendations(user_profile)
        recommendations.extend(goal_recommendations)
        
        return {
            'recommendations': recommendations,
            'portfolio_suggestions': self._generate_portfolio_suggestions(user_profile),
            'next_steps': self._generate_next_steps(user_profile)
        }
    
    def _calculate_product_score(self, product, user_profile):
        """Calculate relevance score for a product based on user profile"""
        score = 50  # Base score
        
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        age = user_profile.get('age', 30)
        income = user_profile.get('annual_income', 50000)
        experience = user_profile.get('investment_experience', 'Beginner')
        
        # Risk alignment scoring
        risk_map = {'Conservative': 'Low', 'Moderate': 'Moderate', 'Aggressive': 'High'}
        expected_risk = risk_map.get(risk_tolerance, 'Moderate')
        
        if product['risk_level'] == expected_risk:
            score += 20
        elif abs(['Very Low', 'Low', 'Moderate', 'Moderate-High', 'High'].index(product['risk_level']) - 
                ['Very Low', 'Low', 'Moderate', 'Moderate-High', 'High'].index(expected_risk)) <= 1:
            score += 10
        else:
            score -= 10
        
        # Experience-based scoring
        if experience == 'Beginner' and product['type'] in ['Target Date Fund', 'Stock ETF', 'Bond ETF']:
            score += 15
        elif experience == 'Advanced' and product['type'] in ['Growth Stock ETF', 'Small-Cap ETF']:
            score += 10
        
        # Age-based scoring
        if age < 30 and product['risk_level'] in ['Moderate-High', 'High']:
            score += 10
        elif age > 50 and product['risk_level'] in ['Low', 'Moderate']:
            score += 10
        
        # Income-based scoring
        if income < 50000 and product['min_investment'] <= 100:
            score += 5
        elif income > 100000 and product['expense_ratio'] < 0.1:
            score += 5
        
        return min(100, max(0, score))
    
    def _generate_product_reasoning(self, product, user_profile):
        """Generate reasoning for why a product is recommended"""
        reasons = []
        
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        age = user_profile.get('age', 30)
        experience = user_profile.get('investment_experience', 'Beginner')
        
        # Risk alignment
        if risk_tolerance == 'Conservative' and product['risk_level'] == 'Low':
            reasons.append("Matches your conservative risk tolerance")
        elif risk_tolerance == 'Aggressive' and product['risk_level'] == 'High':
            reasons.append("Aligns with your aggressive investment approach")
        
        # Low cost
        if product['expense_ratio'] <= 0.05:
            reasons.append("Very low expense ratio helps maximize returns")
        
        # Liquidity
        if product['liquidity'] == 'High':
            reasons.append("High liquidity provides flexibility")
        
        # Experience level
        if experience == 'Beginner' and product['type'] in ['Target Date Fund', 'Stock ETF']:
            reasons.append("Good for beginning investors")
        
        # Age appropriateness
        if age < 35 and product['risk_level'] in ['Moderate-High', 'High']:
            reasons.append("Suitable for your age and long investment horizon")
        elif age > 50 and product['risk_level'] in ['Low', 'Moderate']:
            reasons.append("Conservative approach appropriate as you near retirement")
        
        return reasons
    
    def _suggest_allocation(self, product, user_profile):
        """Suggest allocation percentage for a product"""
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        age = user_profile.get('age', 30)
        
        # Base allocation suggestions
        if product['type'] == 'Target Date Fund':
            return f"50-70% of portfolio (core holding)"
        elif product['type'] == 'Stock ETF':
            if risk_tolerance == 'Conservative':
                return f"20-40% of portfolio"
            elif risk_tolerance == 'Moderate':
                return f"40-60% of portfolio"
            else:
                return f"60-80% of portfolio"
        elif product['type'] == 'Bond ETF':
            bond_allocation = min(age, 40)  # Age in bonds rule, capped at 40%
            return f"{bond_allocation-10}-{bond_allocation+10}% of portfolio"
        elif product['type'] == 'Cash Equivalent':
            return f"5-15% of portfolio (emergency fund)"
        else:
            return f"5-20% of portfolio (satellite holding)"
    
    def _get_goal_specific_recommendations(self, user_profile):
        """Get recommendations specific to user's financial goals"""
        goals = user_profile.get('financial_goals', [])
        goal_recommendations = []
        
        for goal in goals:
            if goal == 'Emergency Fund':
                rec = {
                    'product': {
                        'name': 'High-Yield Savings Account',
                        'type': 'Cash Equivalent',
                        'risk_level': 'Very Low',
                        'description': 'FDIC insured emergency fund'
                    },
                    'reasoning': ['Essential for financial security', 'Immediate access to funds'],
                    'allocation_suggestion': '3-6 months of expenses',
                    'goal_specific': True
                }
                goal_recommendations.append(rec)
            
            elif goal == 'Retirement Planning':
                rec = {
                    'product': {
                        'name': '401(k) or IRA Contributions',
                        'type': 'Retirement Account',
                        'risk_level': 'Varies',
                        'description': 'Tax-advantaged retirement savings'
                    },
                    'reasoning': ['Tax benefits', 'Employer matching', 'Long-term growth'],
                    'allocation_suggestion': '10-15% of income minimum',
                    'goal_specific': True
                }
                goal_recommendations.append(rec)
            
            elif goal == 'Home Purchase':
                rec = {
                    'product': {
                        'name': 'Conservative Investment Mix',
                        'type': 'Mixed Portfolio',
                        'risk_level': 'Low-Moderate',
                        'description': 'Capital preservation for down payment'
                    },
                    'reasoning': ['Capital preservation', 'Liquidity for purchase'],
                    'allocation_suggestion': '70% bonds, 30% stocks',
                    'goal_specific': True
                }
                goal_recommendations.append(rec)
        
        return goal_recommendations
    
    def _generate_portfolio_suggestions(self, user_profile):
        """Generate overall portfolio allocation suggestions"""
        age = user_profile.get('age', 30)
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        
        # Basic asset allocation based on age and risk tolerance
        if risk_tolerance == 'Conservative':
            stock_allocation = max(30, 70 - age)
        elif risk_tolerance == 'Moderate':
            stock_allocation = max(40, 100 - age)
        else:  # Aggressive
            stock_allocation = max(60, 120 - age)
        
        bond_allocation = min(60, 100 - stock_allocation)
        
        suggestions = {
            'asset_allocation': {
                'stocks': stock_allocation,
                'bonds': bond_allocation,
                'alternatives': 5,
                'cash': 5
            },
            'diversification_tips': [
                'Include both domestic and international exposure',
                'Consider small-cap and large-cap stocks',
                'Include both growth and value styles',
                'Rebalance quarterly or when allocations drift >5%'
            ],
            'implementation_order': [
                '1. Build emergency fund (3-6 months expenses)',
                '2. Maximize employer 401(k) match',
                '3. Pay off high-interest debt',
                '4. Build diversified portfolio',
                '5. Consider tax-loss harvesting'
            ]
        }
        
        return suggestions
    
    def _generate_next_steps(self, user_profile):
        """Generate actionable next steps"""
        steps = []
        
        income = user_profile.get('annual_income', 0)
        debt = user_profile.get('debt_amount', 0)
        monthly_savings = user_profile.get('monthly_savings', 0)
        
        # Emergency fund check
        monthly_expenses = (income - monthly_savings * 12) / 12
        emergency_fund_target = monthly_expenses * 6
        
        if monthly_savings == 0:
            steps.append("Start by setting up automatic savings of at least 10% of income")
        
        if debt > income * 0.3:
            steps.append("Focus on paying down high-interest debt before aggressive investing")
        
        steps.append("Open a high-yield savings account for emergency fund")
        steps.append("Research low-cost brokerages (Vanguard, Fidelity, Schwab)")
        steps.append("Start with target-date funds or broad market ETFs")
        steps.append("Set up automatic investing to dollar-cost average")
        
        return steps
    
    def _get_insurance_recommendations(self, user_profile):
        """Generate insurance recommendations"""
        recommendations = []
        
        age = user_profile.get('age', 30)
        income = user_profile.get('annual_income', 50000)
        debt = user_profile.get('debt_amount', 0)
        employment = user_profile.get('employment_status', 'Employed')
        goals = user_profile.get('financial_goals', [])
        
        # Life insurance recommendations
        life_insurance_need = income * 10 + debt
        
        if age < 40:
            rec = {
                'product': {
                    'name': 'Term Life Insurance (20-30 years)',
                    'type': 'Life Insurance',
                    'coverage_amount': life_insurance_need,
                    'estimated_cost': f"${(life_insurance_need / 1000) * 1.5:.0f}/month"
                },
                'reasoning': [
                    'Most cost-effective at your age',
                    'Covers income replacement needs',
                    'Protects family from debt burden'
                ],
                'priority': 'High' if debt > 0 or 'Home Purchase' in goals else 'Medium'
            }
            recommendations.append(rec)
        
        # Disability insurance
        if employment == 'Employed' and income > 30000:
            rec = {
                'product': {
                    'name': 'Long-Term Disability Insurance',
                    'type': 'Disability Insurance',
                    'coverage_amount': income * 0.6,
                    'estimated_cost': f"${income * 0.02 / 12:.0f}/month"
                },
                'reasoning': [
                    'Protects future earning capacity',
                    'More likely to become disabled than die',
                    'Employer coverage may be insufficient'
                ],
                'priority': 'High'
            }
            recommendations.append(rec)
        
        return {
            'recommendations': recommendations,
            'coverage_gaps': self._identify_coverage_gaps(user_profile),
            'cost_optimization': self._suggest_cost_optimization(user_profile)
        }
    
    def _identify_coverage_gaps(self, user_profile):
        """Identify potential insurance coverage gaps"""
        gaps = []
        
        employment = user_profile.get('employment_status', 'Employed')
        age = user_profile.get('age', 30)
        income = user_profile.get('annual_income', 0)
        
        if employment != 'Employed':
            gaps.append("Health insurance may not be employer-provided")
        
        if age > 30 and income > 50000:
            gaps.append("Consider umbrella liability insurance for asset protection")
        
        if 'Home Purchase' in user_profile.get('financial_goals', []):
            gaps.append("Will need homeowners insurance when purchasing property")
        
        return gaps
    
    def _suggest_cost_optimization(self, user_profile):
        """Suggest ways to optimize insurance costs"""
        tips = [
            "Bundle auto and home insurance for discounts",
            "Increase deductibles to lower premiums",
            "Shop around annually for better rates",
            "Maintain good credit score for better rates",
            "Consider term life insurance over whole life for most people"
        ]
        
        age = user_profile.get('age', 30)
        if age < 35:
            tips.append("Lock in term life insurance rates while young and healthy")
        
        return tips
    
    def _get_comprehensive_recommendations(self, user_profile):
        """Get comprehensive financial recommendations"""
        investment_recs = self._get_investment_recommendations(user_profile)
        insurance_recs = self._get_insurance_recommendations(user_profile)
        
        return {
            'investment_recommendations': investment_recs,
            'insurance_recommendations': insurance_recs,
            'priority_matrix': self._create_priority_matrix(user_profile),
            'action_plan': self._create_action_plan(user_profile)
        }
    
    def _create_priority_matrix(self, user_profile):
        """Create priority matrix for financial decisions"""
        income = user_profile.get('annual_income', 0)
        debt = user_profile.get('debt_amount', 0)
        monthly_savings = user_profile.get('monthly_savings', 0)
        
        priorities = []
        
        # Emergency fund
        if monthly_savings * 6 < income / 4:  # Less than 3 months expenses
            priorities.append({'item': 'Emergency Fund', 'priority': 'Critical', 'timeline': 'Immediate'})
        
        # High-interest debt
        if debt > income * 0.3:
            priorities.append({'item': 'Debt Reduction', 'priority': 'High', 'timeline': '1-2 years'})
        
        # Insurance coverage
        priorities.append({'item': 'Basic Insurance Coverage', 'priority': 'High', 'timeline': 'Within 3 months'})
        
        # Retirement savings
        priorities.append({'item': 'Retirement Contributions', 'priority': 'Medium', 'timeline': 'Ongoing'})
        
        # Investment portfolio
        priorities.append({'item': 'Investment Portfolio', 'priority': 'Medium', 'timeline': '6-12 months'})
        
        return sorted(priorities, key=lambda x: {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3}[x['priority']])
    
    def _create_action_plan(self, user_profile):
        """Create step-by-step action plan"""
        plan = {
            'month_1': [
                'Open high-yield savings account',
                'Set up automatic savings transfer',
                'Research insurance needs and get quotes'
            ],
            'month_2': [
                'Purchase necessary insurance coverage',
                'Create budget and expense tracking system',
                'Research investment account options'
            ],
            'month_3': [
                'Open investment account with low-cost provider',
                'Set up automatic investment contributions',
                'Begin building emergency fund'
            ],
            'month_6': [
                'Review and rebalance investment portfolio',
                'Assess progress toward financial goals',
                'Consider increasing savings rate'
            ],
            'annually': [
                'Review insurance coverage and needs',
                'Rebalance investment portfolio',
                'Update financial goals and plans',
                'Tax planning and optimization'
            ]
        }
        
        return plan
    
    def generate_user_segments(self, user_profiles):
        """Segment users for collaborative filtering (when multiple users exist)"""
        if len(user_profiles) < 5:
            return None  # Need minimum users for clustering
        
        # Feature extraction for clustering
        features = []
        for profile in user_profiles:
            feature_vector = [
                profile.get('age', 30),
                profile.get('annual_income', 50000),
                profile.get('monthly_savings', 500),
                profile.get('debt_amount', 0),
                {'Conservative': 0, 'Moderate': 1, 'Aggressive': 2}.get(profile.get('risk_tolerance', 'Moderate'), 1),
                {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}.get(profile.get('investment_experience', 'Beginner'), 0)
            ]
            features.append(feature_vector)
        
        # Normalize features
        features_scaled = self.scaler.fit_transform(features)
        
        # Perform clustering
        n_clusters = min(3, len(user_profiles) // 2)  # 3 clusters max
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(features_scaled)
        
        self.user_clusters = clusters
        self.is_fitted = True
        
        return clusters
    
    def get_collaborative_recommendations(self, user_profile, all_user_profiles):
        """Get recommendations based on similar users (collaborative filtering)"""
        if not self.is_fitted or len(all_user_profiles) < 5:
            return self.get_personalized_recommendations(user_profile)
        
        # Find similar users
        similar_users = self._find_similar_users(user_profile, all_user_profiles)
        
        # Aggregate their preferences/choices
        recommendations = self._aggregate_similar_user_preferences(similar_users)
        
        return recommendations
    
    def _find_similar_users(self, target_user, all_users):
        """Find users similar to target user"""
        target_features = [
            target_user.get('age', 30),
            target_user.get('annual_income', 50000),
            target_user.get('monthly_savings', 500),
            target_user.get('debt_amount', 0),
            {'Conservative': 0, 'Moderate': 1, 'Aggressive': 2}.get(target_user.get('risk_tolerance', 'Moderate'), 1),
            {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}.get(target_user.get('investment_experience', 'Beginner'), 0)
        ]
        
        similar_users = []
        for user in all_users:
            user_features = [
                user.get('age', 30),
                user.get('annual_income', 50000),
                user.get('monthly_savings', 500),
                user.get('debt_amount', 0),
                {'Conservative': 0, 'Moderate': 1, 'Aggressive': 2}.get(user.get('risk_tolerance', 'Moderate'), 1),
                {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}.get(user.get('investment_experience', 'Beginner'), 0)
            ]
            
            # Calculate similarity (you could use cosine similarity or other metrics)
            similarity = cosine_similarity([target_features], [user_features])[0][0]
            if similarity > 0.8:  # High similarity threshold
                similar_users.append(user)
        
        return similar_users
    
    def _aggregate_similar_user_preferences(self, similar_users):
        """Aggregate preferences from similar users"""
        # This would normally look at actual investment choices/preferences
        # For now, return personalized recommendations
        if similar_users:
            # Use the most common risk tolerance among similar users
            risk_tolerances = [user.get('risk_tolerance', 'Moderate') for user in similar_users]
            most_common_risk = max(set(risk_tolerances), key=risk_tolerances.count)
            
            # Create a composite profile
            composite_profile = similar_users[0].copy()
            composite_profile['risk_tolerance'] = most_common_risk
            
            return self.get_personalized_recommendations(composite_profile)
        
        return {'recommendations': [], 'message': 'No similar users found'}
