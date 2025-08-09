"""
Mock user data for testing collaborative filtering and recommendation systems.
This data represents realistic user profiles for testing purposes only.
"""

from datetime import datetime, timedelta
import random

# Set random seed for consistent data generation
random.seed(42)

def generate_mock_users():
    """Generate a diverse set of realistic user profiles for testing"""
    
    mock_users = [
        # Young Professionals (22-35)
        {
            'name': 'Alex Thompson',
            'age': 28,
            'annual_income': 75000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Aggressive',
            'investment_experience': 'Intermediate',
            'monthly_savings': 1200,
            'debt_amount': 25000,
            'financial_goals': ['Emergency Fund', 'Retirement Planning', 'Investment Growth'],
            'created_date': (datetime.now() - timedelta(days=120)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=30)).isoformat(),
            'profile_id': 'usr_001'
        },
        {
            'name': 'Sarah Chen',
            'age': 26,
            'annual_income': 68000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Beginner',
            'monthly_savings': 1000,
            'debt_amount': 35000,
            'financial_goals': ['Emergency Fund', 'Debt Reduction', 'Home Purchase'],
            'created_date': (datetime.now() - timedelta(days=90)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=15)).isoformat(),
            'profile_id': 'usr_002'
        },
        {
            'name': 'Marcus Johnson',
            'age': 32,
            'annual_income': 95000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Aggressive',
            'investment_experience': 'Advanced',
            'monthly_savings': 2000,
            'debt_amount': 15000,
            'financial_goals': ['Investment Growth', 'Retirement Planning', 'Home Purchase'],
            'created_date': (datetime.now() - timedelta(days=200)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=5)).isoformat(),
            'profile_id': 'usr_003'
        },
        {
            'name': 'Emily Rodriguez',
            'age': 29,
            'annual_income': 82000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Intermediate',
            'monthly_savings': 1500,
            'debt_amount': 20000,
            'financial_goals': ['Emergency Fund', 'Retirement Planning', 'Education'],
            'created_date': (datetime.now() - timedelta(days=150)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=20)).isoformat(),
            'profile_id': 'usr_004'
        },
        
        # Mid-Career Professionals (35-50)
        {
            'name': 'David Kim',
            'age': 42,
            'annual_income': 120000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Advanced',
            'monthly_savings': 3000,
            'debt_amount': 180000,  # Mortgage
            'financial_goals': ['Retirement Planning', 'Education', 'Investment Growth'],
            'created_date': (datetime.now() - timedelta(days=300)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=10)).isoformat(),
            'profile_id': 'usr_005'
        },
        {
            'name': 'Jennifer Walsh',
            'age': 38,
            'annual_income': 105000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Intermediate',
            'monthly_savings': 2200,
            'debt_amount': 45000,
            'financial_goals': ['Emergency Fund', 'Retirement Planning', 'Education'],
            'created_date': (datetime.now() - timedelta(days=180)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=25)).isoformat(),
            'profile_id': 'usr_006'
        },
        {
            'name': 'Robert Martinez',
            'age': 45,
            'annual_income': 140000,
            'employment_status': 'Self-Employed',
            'risk_tolerance': 'Aggressive',
            'investment_experience': 'Advanced',
            'monthly_savings': 4000,
            'debt_amount': 60000,
            'financial_goals': ['Retirement Planning', 'Investment Growth', 'Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=400)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=8)).isoformat(),
            'profile_id': 'usr_007'
        },
        {
            'name': 'Lisa Anderson',
            'age': 40,
            'annual_income': 98000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Intermediate',
            'monthly_savings': 2500,
            'debt_amount': 25000,
            'financial_goals': ['Retirement Planning', 'Home Purchase', 'Education'],
            'created_date': (datetime.now() - timedelta(days=220)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=12)).isoformat(),
            'profile_id': 'usr_008'
        },
        
        # Pre-Retirement (50-65)
        {
            'name': 'Michael Brown',
            'age': 55,
            'annual_income': 150000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Advanced',
            'monthly_savings': 5000,
            'debt_amount': 80000,
            'financial_goals': ['Retirement Planning', 'Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=500)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=18)).isoformat(),
            'profile_id': 'usr_009'
        },
        {
            'name': 'Patricia Wilson',
            'age': 58,
            'annual_income': 110000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Intermediate',
            'monthly_savings': 4500,
            'debt_amount': 30000,
            'financial_goals': ['Retirement Planning', 'Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=350)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=22)).isoformat(),
            'profile_id': 'usr_010'
        },
        {
            'name': 'James Taylor',
            'age': 52,
            'annual_income': 135000,
            'employment_status': 'Self-Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Advanced',
            'monthly_savings': 3800,
            'debt_amount': 120000,
            'financial_goals': ['Retirement Planning', 'Investment Growth', 'Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=280)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=6)).isoformat(),
            'profile_id': 'usr_011'
        },
        
        # Young Starters (22-28)
        {
            'name': 'Ashley Davis',
            'age': 24,
            'annual_income': 45000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Beginner',
            'monthly_savings': 600,
            'debt_amount': 40000,  # Student loans
            'financial_goals': ['Emergency Fund', 'Debt Reduction'],
            'created_date': (datetime.now() - timedelta(days=60)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=10)).isoformat(),
            'profile_id': 'usr_012'
        },
        {
            'name': 'Kevin Lee',
            'age': 25,
            'annual_income': 52000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Aggressive',
            'investment_experience': 'Beginner',
            'monthly_savings': 800,
            'debt_amount': 35000,
            'financial_goals': ['Emergency Fund', 'Investment Growth', 'Debt Reduction'],
            'created_date': (datetime.now() - timedelta(days=45)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=7)).isoformat(),
            'profile_id': 'usr_013'
        },
        {
            'name': 'Samantha Garcia',
            'age': 27,
            'annual_income': 58000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Beginner',
            'monthly_savings': 700,
            'debt_amount': 28000,
            'financial_goals': ['Emergency Fund', 'Home Purchase', 'Debt Reduction'],
            'created_date': (datetime.now() - timedelta(days=75)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=14)).isoformat(),
            'profile_id': 'usr_014'
        },
        
        # High Earners
        {
            'name': 'Christopher White',
            'age': 35,
            'annual_income': 180000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Aggressive',
            'investment_experience': 'Advanced',
            'monthly_savings': 6000,
            'debt_amount': 250000,  # High-value mortgage
            'financial_goals': ['Investment Growth', 'Retirement Planning', 'Education'],
            'created_date': (datetime.now() - timedelta(days=320)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=4)).isoformat(),
            'profile_id': 'usr_015'
        },
        {
            'name': 'Rachel Thompson',
            'age': 33,
            'annual_income': 165000,
            'employment_status': 'Self-Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Advanced',
            'monthly_savings': 5500,
            'debt_amount': 90000,
            'financial_goals': ['Retirement Planning', 'Investment Growth', 'Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=240)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=16)).isoformat(),
            'profile_id': 'usr_016'
        },
        
        # Lower Income / Students
        {
            'name': 'Daniel Miller',
            'age': 23,
            'annual_income': 35000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Beginner',
            'monthly_savings': 300,
            'debt_amount': 45000,  # Student loans
            'financial_goals': ['Emergency Fund', 'Debt Reduction'],
            'created_date': (datetime.now() - timedelta(days=50)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=12)).isoformat(),
            'profile_id': 'usr_017'
        },
        {
            'name': 'Nicole Jackson',
            'age': 26,
            'annual_income': 42000,
            'employment_status': 'Employed',
            'risk_tolerance': 'Moderate',
            'investment_experience': 'Beginner',
            'monthly_savings': 450,
            'debt_amount': 32000,
            'financial_goals': ['Emergency Fund', 'Debt Reduction', 'Home Purchase'],
            'created_date': (datetime.now() - timedelta(days=80)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=9)).isoformat(),
            'profile_id': 'usr_018'
        },
        
        # Retirees
        {
            'name': 'William Johnson',
            'age': 67,
            'annual_income': 65000,  # Retirement income
            'employment_status': 'Retired',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Intermediate',
            'monthly_savings': 1000,
            'debt_amount': 0,
            'financial_goals': ['Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=600)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=30)).isoformat(),
            'profile_id': 'usr_019'
        },
        {
            'name': 'Margaret Davis',
            'age': 63,
            'annual_income': 85000,
            'employment_status': 'Retired',
            'risk_tolerance': 'Conservative',
            'investment_experience': 'Advanced',
            'monthly_savings': 2000,
            'debt_amount': 15000,
            'financial_goals': ['Emergency Fund'],
            'created_date': (datetime.now() - timedelta(days=450)).isoformat(),
            'last_updated': (datetime.now() - timedelta(days=35)).isoformat(),
            'profile_id': 'usr_020'
        }
    ]
    
    return mock_users

def get_users_by_segment():
    """Get users organized by demographic/financial segments"""
    users = generate_mock_users()
    
    segments = {
        'Young Professional': [],
        'Conservative Saver': [],
        'Aggressive Investor': [],
        'Pre-Retirement': [],
        'Family Focused': [],
        'Balanced Investor': []
    }
    
    for user in users:
        age = user['age']
        income = user['annual_income']
        risk_tolerance = user['risk_tolerance']
        experience = user['investment_experience']
        goals = user['financial_goals']
        
        # Categorize users
        if age < 35 and income > 60000:
            segments['Young Professional'].append(user)
        elif risk_tolerance == 'Conservative' or experience == 'Beginner':
            segments['Conservative Saver'].append(user)
        elif risk_tolerance == 'Aggressive' and experience in ['Intermediate', 'Advanced']:
            segments['Aggressive Investor'].append(user)
        elif age >= 50:
            segments['Pre-Retirement'].append(user)
        elif 'Home Purchase' in goals or 'Education' in goals:
            segments['Family Focused'].append(user)
        else:
            segments['Balanced Investor'].append(user)
    
    return segments

def get_similar_users(target_user, all_users=None):
    """Find users similar to a target user profile"""
    if all_users is None:
        all_users = generate_mock_users()
    
    similar_users = []
    target_age = target_user.get('age', 30)
    target_income = target_user.get('annual_income', 50000)
    target_risk = target_user.get('risk_tolerance', 'Moderate')
    
    for user in all_users:
        # Skip if same user
        if user.get('profile_id') == target_user.get('profile_id'):
            continue
        
        # Calculate similarity score
        age_diff = abs(user.get('age', 30) - target_age)
        income_diff = abs(user.get('annual_income', 50000) - target_income) / max(target_income, 1)
        risk_match = 1 if user.get('risk_tolerance') == target_risk else 0
        
        # Similarity score (lower is more similar)
        similarity_score = age_diff * 0.3 + income_diff * 100 * 0.5 + (1 - risk_match) * 20
        
        if similarity_score < 15:  # Threshold for similarity
            similar_users.append({
                'user': user,
                'similarity_score': similarity_score
            })
    
    # Sort by similarity score (most similar first)
    similar_users.sort(key=lambda x: x['similarity_score'])
    
    return [item['user'] for item in similar_users[:5]]  # Return top 5 similar users

def get_user_statistics():
    """Get statistical overview of mock user data"""
    users = generate_mock_users()
    
    stats = {
        'total_users': len(users),
        'age_distribution': {
            '20-29': len([u for u in users if 20 <= u['age'] <= 29]),
            '30-39': len([u for u in users if 30 <= u['age'] <= 39]),
            '40-49': len([u for u in users if 40 <= u['age'] <= 49]),
            '50-59': len([u for u in users if 50 <= u['age'] <= 59]),
            '60+': len([u for u in users if u['age'] >= 60])
        },
        'risk_tolerance_distribution': {
            'Conservative': len([u for u in users if u['risk_tolerance'] == 'Conservative']),
            'Moderate': len([u for u in users if u['risk_tolerance'] == 'Moderate']),
            'Aggressive': len([u for u in users if u['risk_tolerance'] == 'Aggressive'])
        },
        'experience_distribution': {
            'Beginner': len([u for u in users if u['investment_experience'] == 'Beginner']),
            'Intermediate': len([u for u in users if u['investment_experience'] == 'Intermediate']),
            'Advanced': len([u for u in users if u['investment_experience'] == 'Advanced'])
        },
        'employment_distribution': {
            'Employed': len([u for u in users if u['employment_status'] == 'Employed']),
            'Self-Employed': len([u for u in users if u['employment_status'] == 'Self-Employed']),
            'Retired': len([u for u in users if u['employment_status'] == 'Retired'])
        },
        'income_statistics': {
            'average': sum([u['annual_income'] for u in users]) / len(users),
            'median': sorted([u['annual_income'] for u in users])[len(users)//2],
            'min': min([u['annual_income'] for u in users]),
            'max': max([u['annual_income'] for u in users])
        },
        'common_goals': {}
    }
    
    # Calculate common goals
    all_goals = []
    for user in users:
        all_goals.extend(user.get('financial_goals', []))
    
    goal_counts = {}
    for goal in all_goals:
        goal_counts[goal] = goal_counts.get(goal, 0) + 1
    
    stats['common_goals'] = dict(sorted(goal_counts.items(), key=lambda x: x[1], reverse=True))
    
    return stats

# Example usage functions
def get_test_user_profiles(count=5):
    """Get a subset of users for testing"""
    users = generate_mock_users()
    return users[:count]

def get_diverse_test_set():
    """Get a diverse set of users covering different segments"""
    users = generate_mock_users()
    diverse_set = []
    
    # Get one user from each major category
    categories = {
        'young_aggressive': lambda u: u['age'] < 30 and u['risk_tolerance'] == 'Aggressive',
        'mid_conservative': lambda u: 30 <= u['age'] < 50 and u['risk_tolerance'] == 'Conservative',
        'pre_retirement': lambda u: u['age'] >= 50,
        'high_earner': lambda u: u['annual_income'] > 120000,
        'beginner': lambda u: u['investment_experience'] == 'Beginner'
    }
    
    for category, condition in categories.items():
        matching_users = [u for u in users if condition(u)]
        if matching_users:
            diverse_set.append(matching_users[0])
    
    return diverse_set
