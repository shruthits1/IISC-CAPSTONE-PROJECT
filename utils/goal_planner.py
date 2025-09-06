import numpy as np
from datetime import datetime, timedelta
import math

class GoalPlanner:
    def __init__(self):
        self.inflation_rate = 0.03  # 3% annual inflation
        self.market_return = 0.07   # 7% average market return
    
    def create_goal_plan(self, goal_name, target_amount, timeline_years, priority, user_profile):
        """Create a comprehensive goal plan"""
        
        # Adjust for inflation
        future_value_needed = self._calculate_future_value(target_amount, timeline_years)
        
        # Calculate required monthly savings
        monthly_savings_needed = self._calculate_monthly_savings(future_value_needed, timeline_years)
        
        # Assess feasibility
        feasibility = self._assess_feasibility(monthly_savings_needed, user_profile)
        
        # Generate recommendations
        recommendations = self._generate_goal_recommendations(
            goal_name, target_amount, timeline_years, monthly_savings_needed, user_profile, feasibility
        )
        
        # Create investment strategy
        investment_strategy = self._create_investment_strategy(timeline_years, user_profile)
        
        return {
            'goal_name': goal_name,
            'target_amount': target_amount,
            'future_value_needed': future_value_needed,
            'timeline_years': timeline_years,
            'monthly_savings_needed': monthly_savings_needed,
            'feasibility': feasibility,
            'recommendations': recommendations,
            'investment_strategy': investment_strategy,
            'priority': priority
        }
    
    def _calculate_future_value(self, present_value, years):
        """Calculate future value accounting for inflation"""
        return present_value * ((1 + self.inflation_rate) ** years)
    
    def _calculate_monthly_savings(self, future_value, years):
        """Calculate monthly savings needed using compound interest"""
        months = years * 12
        monthly_rate = self.market_return / 12
        
        # PMT formula for annuity
        if monthly_rate > 0:
            monthly_payment = future_value * monthly_rate / (((1 + monthly_rate) ** months) - 1)
        else:
            monthly_payment = future_value / months
        
        return monthly_payment
    
    def _assess_feasibility(self, monthly_savings_needed, user_profile):
        """Assess if the goal is feasible given user's financial situation"""
        available_savings = user_profile.get('monthly_savings', 0)
        current_income = user_profile.get('annual_income', 0) / 12
        
        # Calculate what percentage of savings this goal would require
        if available_savings > 0:
            savings_percentage = (monthly_savings_needed / available_savings) * 100
        else:
            savings_percentage = float('inf')
        
        # Calculate what percentage of income this would be
        income_percentage = (monthly_savings_needed / current_income) * 100 if current_income > 0 else float('inf')
        
        if monthly_savings_needed <= available_savings * 0.3:
            return "Highly Feasible - Can be achieved with 30% or less of current savings"
        elif monthly_savings_needed <= available_savings * 0.6:
            return "Feasible - Requires 30-60% of current savings capacity"
        elif monthly_savings_needed <= available_savings:
            return "Challenging - Requires most of your current savings capacity"
        elif income_percentage <= 20:
            return "Requires Income Increase - Need to boost savings rate"
        else:
            return "Very Challenging - May need to extend timeline or reduce target amount"
    
    def _generate_goal_recommendations(self, goal_name, target_amount, timeline_years, monthly_savings, user_profile, feasibility):
        """Generate specific recommendations for achieving the goal"""
        recommendations = []
        
        # Timeline-based recommendations
        if timeline_years < 2:
            recommendations.append("Short timeline - Focus on high-yield savings accounts and CDs for capital preservation")
            recommendations.append("Avoid volatile investments due to short time horizon")
        elif timeline_years < 5:
            recommendations.append("Medium timeline - Consider balanced portfolio with 60% stocks, 40% bonds")
            recommendations.append("Use tax-advantaged accounts if applicable")
        else:
            recommendations.append("Long timeline - Take advantage of compound growth with stock-heavy portfolio")
            recommendations.append("Consider aggressive growth investments for early years")
        
        # Amount-based recommendations
        if target_amount > 100000:
            recommendations.append("Large goal - Break into smaller milestones to track progress")
            recommendations.append("Consider multiple investment accounts and strategies")
        
        # Feasibility-based recommendations
        if "Very Challenging" in feasibility or "Requires Income Increase" in feasibility:
            recommendations.append("Consider extending the timeline to make monthly savings more manageable")
            recommendations.append("Look for ways to increase income or reduce expenses")
            recommendations.append("Explore side income opportunities")
        elif "Challenging" in feasibility:
            recommendations.append("Automate savings to ensure consistent contributions")
            recommendations.append("Review and optimize your budget to free up more savings")
        
        # Goal-specific recommendations
        goal_lower = goal_name.lower()
        if "emergency" in goal_lower:
            recommendations.append("Keep emergency funds in liquid, low-risk accounts (high-yield savings)")
            recommendations.append("Target 3-6 months of living expenses")
        elif "house" in goal_lower or "home" in goal_lower:
            recommendations.append("Consider first-time homebuyer programs and assistance")
            recommendations.append("Save for down payment in conservative investments")
            recommendations.append("Don't forget closing costs (2-5% of home price)")
        elif "retirement" in goal_lower:
            recommendations.append("Maximize employer 401(k) match first")
            recommendations.append("Consider Roth IRA for tax-free growth")
            recommendations.append("Use age-based target-date funds for automatic rebalancing")
        elif "education" in goal_lower:
            recommendations.append("Look into 529 education savings plans for tax advantages")
            recommendations.append("Research scholarships and financial aid options")
        
        # Risk tolerance recommendations
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        if risk_tolerance == 'Conservative':
            recommendations.append("Focus on capital preservation with bonds and CDs")
            recommendations.append("Accept lower returns for stability")
        elif risk_tolerance == 'Aggressive':
            recommendations.append("Consider higher allocation to growth stocks and equity funds")
            recommendations.append("Take advantage of market volatility for dollar-cost averaging")
        
        # Age-based recommendations
        age = user_profile.get('age', 30)
        if age < 30:
            recommendations.append("Take advantage of time - consider aggressive growth strategies")
        elif age > 50:
            recommendations.append("Balance growth with capital preservation as you near retirement")
        
        return recommendations
    
    def _create_investment_strategy(self, timeline_years, user_profile):
        """Create appropriate investment strategy based on timeline and profile"""
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        age = user_profile.get('age', 30)
        
        strategy = {
            'time_horizon': timeline_years,
            'risk_level': risk_tolerance,
            'recommended_allocation': {},
            'investment_vehicles': [],
            'rebalancing_frequency': 'Quarterly'
        }
        
        # Determine asset allocation based on timeline and risk tolerance
        if timeline_years < 2:
            # Short-term: Capital preservation
            strategy['recommended_allocation'] = {
                'Cash/CDs': 70,
                'High-Yield Savings': 20,
                'Short-term Bonds': 10
            }
            strategy['investment_vehicles'] = [
                'High-yield savings accounts',
                'Certificates of Deposit (CDs)',
                'Money market accounts',
                'Short-term treasury bills'
            ]
        elif timeline_years < 5:
            # Medium-term: Balanced approach
            if risk_tolerance == 'Conservative':
                allocation = {'Bonds': 60, 'Stocks': 30, 'Cash': 10}
            elif risk_tolerance == 'Aggressive':
                allocation = {'Stocks': 70, 'Bonds': 25, 'Cash': 5}
            else:  # Moderate
                allocation = {'Stocks': 50, 'Bonds': 40, 'Cash': 10}
            
            strategy['recommended_allocation'] = allocation
            strategy['investment_vehicles'] = [
                'Target-date funds',
                'Balanced mutual funds',
                'Bond index funds',
                'Broad market ETFs'
            ]
        else:
            # Long-term: Growth focus
            if risk_tolerance == 'Conservative':
                allocation = {'Stocks': 50, 'Bonds': 40, 'Real Estate': 5, 'Cash': 5}
            elif risk_tolerance == 'Aggressive':
                allocation = {'Stocks': 85, 'Bonds': 10, 'Real Estate': 5}
            else:  # Moderate
                allocation = {'Stocks': 70, 'Bonds': 25, 'Real Estate': 5}
            
            strategy['recommended_allocation'] = allocation
            strategy['investment_vehicles'] = [
                'Low-cost index funds',
                'ETFs (Exchange-Traded Funds)',
                'Target-date funds',
                'Real Estate Investment Trusts (REITs)',
                'International diversified funds'
            ]
        
        return strategy
    
    def calculate_goal_progress(self, current_amount, monthly_contribution, timeline_remaining, target_amount):
        """Calculate progress towards goal and project completion"""
        
        # Calculate if on track
        months_remaining = timeline_remaining * 12
        monthly_rate = self.market_return / 12
        
        # Future value of current amount
        future_current = current_amount * ((1 + monthly_rate) ** months_remaining)
        
        # Future value of monthly contributions
        if monthly_rate > 0:
            future_contributions = monthly_contribution * (((1 + monthly_rate) ** months_remaining) - 1) / monthly_rate
        else:
            future_contributions = monthly_contribution * months_remaining
        
        projected_total = future_current + future_contributions
        
        # Calculate percentage to goal
        progress_percentage = (projected_total / target_amount) * 100
        
        # Determine status
        if progress_percentage >= 100:
            status = "On Track"
        elif progress_percentage >= 90:
            status = "Slightly Behind"
        elif progress_percentage >= 75:
            status = "Behind"
        else:
            status = "Significantly Behind"
        
        return {
            'current_amount': current_amount,
            'projected_total': projected_total,
            'target_amount': target_amount,
            'progress_percentage': progress_percentage,
            'status': status,
            'shortfall': max(0, target_amount - projected_total),
            'surplus': max(0, projected_total - target_amount)
        }
    
    def optimize_multiple_goals(self, goals, user_profile):
        """Optimize savings allocation across multiple goals"""
        available_monthly_savings = user_profile.get('monthly_savings', 0)
        
        # Prioritize goals
        priority_map = {'High': 3, 'Medium': 2, 'Low': 1}
        
        # Sort by priority and timeline
        sorted_goals = sorted(goals, key=lambda x: (
            -priority_map.get(x.get('priority', 'Medium'), 2),  # High priority first
            x.get('timeline_years', 10)  # Shorter timeline first
        ))
        
        allocation_plan = []
        remaining_budget = available_monthly_savings
        
        for goal in sorted_goals:
            required_monthly = goal.get('monthly_savings_needed', 0)
            
            if remaining_budget >= required_monthly:
                # Can fully fund this goal
                allocation_plan.append({
                    'goal': goal['goal_name'],
                    'allocated_monthly': required_monthly,
                    'percentage_of_budget': (required_monthly / available_monthly_savings) * 100,
                    'status': 'Fully Funded'
                })
                remaining_budget -= required_monthly
            elif remaining_budget > 0:
                # Partially fund this goal
                allocation_plan.append({
                    'goal': goal['goal_name'],
                    'allocated_monthly': remaining_budget,
                    'percentage_of_budget': (remaining_budget / available_monthly_savings) * 100,
                    'status': 'Partially Funded',
                    'funding_ratio': remaining_budget / required_monthly
                })
                remaining_budget = 0
            else:
                # Cannot fund this goal
                allocation_plan.append({
                    'goal': goal['goal_name'],
                    'allocated_monthly': 0,
                    'percentage_of_budget': 0,
                    'status': 'Unfunded'
                })
        
        return {
            'allocation_plan': allocation_plan,
            'total_allocated': available_monthly_savings - remaining_budget,
            'remaining_budget': remaining_budget,
            'recommendations': self._generate_multi_goal_recommendations(allocation_plan, remaining_budget)
        }
    
    def _generate_multi_goal_recommendations(self, allocation_plan, remaining_budget):
        """Generate recommendations for multiple goal management"""
        recommendations = []
        
        unfunded_goals = [goal for goal in allocation_plan if goal['status'] == 'Unfunded']
        partially_funded = [goal for goal in allocation_plan if goal['status'] == 'Partially Funded']
        
        if unfunded_goals:
            recommendations.append(f"You have {len(unfunded_goals)} unfunded goals. Consider increasing savings rate or extending timelines.")
        
        if partially_funded:
            recommendations.append(f"{len(partially_funded)} goals are partially funded. Review priorities and consider adjusting target amounts or timelines.")
        
        if remaining_budget > 0:
            recommendations.append(f"You have ${remaining_budget:.2f} unused monthly savings capacity. Consider allocating to unfunded goals or increasing existing allocations.")
        
        recommendations.append("Review and adjust goal priorities quarterly as your financial situation changes.")
        recommendations.append("Consider automating transfers to separate savings accounts for each goal.")
        
        return recommendations
