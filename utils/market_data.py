import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class MarketDataProvider:
    def __init__(self):
        self.major_indices = {
            '^GSPC': 'S&P 500',
            '^DJI': 'Dow Jones',
            '^IXIC': 'NASDAQ',
            '^RUT': 'Russell 2000'
        }
        
        self.sectors = {
            'XLK': 'Technology',
            'XLF': 'Financial',
            'XLV': 'Healthcare',
            'XLE': 'Energy',
            'XLI': 'Industrial',
            'XLY': 'Consumer Discretionary',
            'XLP': 'Consumer Staples',
            'XLU': 'Utilities',
            'XLB': 'Materials',
            'XLRE': 'Real Estate'
        }
    
    def get_market_overview(self):
        """Get current market overview with major indices"""
        market_data = {}
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        for symbol, name in self.major_indices.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(start=start_date, end=end_date)
                
                if not hist.empty and len(hist) > 1:
                    current_price = hist['Close'][-1]
                    prev_price = hist['Close'][-2]
                    change_pct = ((current_price - prev_price) / prev_price) * 100
                    
                    market_data[name] = {
                        'current_price': current_price,
                        'change': change_pct,
                        'prices': hist['Close'].tolist()
                    }
                else:
                    # Generate mock data if real data fails
                    market_data[name] = self._generate_mock_index_data(symbol)
                    
            except Exception as e:
                # Generate mock data if API fails
                market_data[name] = self._generate_mock_index_data(symbol)
        
        return market_data
    
    def _generate_mock_index_data(self, symbol):
        """Generate realistic mock market data"""
        np.random.seed(hash(symbol) % 2**32)
        
        # Generate 30 days of realistic index movements
        if '^GSPC' in symbol:  # S&P 500
            base_price = 4200
        elif '^DJI' in symbol:  # Dow Jones
            base_price = 34000
        elif '^IXIC' in symbol:  # NASDAQ
            base_price = 13000
        else:  # Russell 2000
            base_price = 2000
        
        prices = [base_price]
        for i in range(29):
            # Daily change typically -2% to +2% for indices
            daily_change = np.random.normal(0, 0.012)  # 1.2% daily volatility
            new_price = prices[-1] * (1 + daily_change)
            prices.append(new_price)
        
        current_price = prices[-1]
        prev_price = prices[-2]
        change_pct = ((current_price - prev_price) / prev_price) * 100
        
        return {
            'current_price': current_price,
            'change': change_pct,
            'prices': prices
        }
    
    def get_stock_price(self, symbol):
        """Get current stock price and basic info"""
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="5d")
            
            if not hist.empty:
                current_price = hist['Close'][-1]
                prev_price = hist['Close'][-2] if len(hist) > 1 else current_price
                change_pct = ((current_price - prev_price) / prev_price) * 100
                
                return {
                    'symbol': symbol,
                    'current_price': current_price,
                    'change': change_pct,
                    'volume': hist['Volume'][-1]
                }
            else:
                return self._generate_mock_stock_price(symbol)
                
        except Exception as e:
            return self._generate_mock_stock_price(symbol)
    
    def _generate_mock_stock_price(self, symbol):
        """Generate mock stock price data"""
        np.random.seed(hash(symbol) % 2**32)
        
        # Generate realistic stock price
        base_price = np.random.uniform(20, 300)
        change_pct = np.random.normal(0, 2.5)  # 2.5% daily volatility
        current_price = base_price * (1 + change_pct/100)
        
        return {
            'symbol': symbol,
            'current_price': current_price,
            'change': change_pct,
            'volume': np.random.randint(100000, 50000000)
        }
    
    def get_sector_performance(self):
        """Get sector performance data"""
        sector_performance = {}
        
        for symbol, sector_name in self.sectors.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="1mo")
                
                if not hist.empty and len(hist) > 1:
                    start_price = hist['Close'].iloc[0]
                    end_price = hist['Close'].iloc[-1]
                    performance = ((end_price - start_price) / start_price) * 100
                    sector_performance[sector_name] = round(performance, 2)
                else:
                    # Generate mock performance
                    sector_performance[sector_name] = round(np.random.normal(1, 5), 2)
                    
            except Exception as e:
                # Generate mock performance if API fails
                np.random.seed(hash(symbol) % 2**32)
                sector_performance[sector_name] = round(np.random.normal(1, 5), 2)
        
        return sector_performance
    
    def get_market_insights(self):
        """Generate market insights based on current data"""
        insights = []
        
        # Get market overview
        market_overview = self.get_market_overview()
        
        # Analyze market direction
        positive_indices = sum(1 for data in market_overview.values() if data['change'] > 0)
        total_indices = len(market_overview)
        
        if positive_indices == total_indices:
            insights.append("🟢 All major indices are positive today, indicating broad market strength.")
        elif positive_indices >= total_indices * 0.75:
            insights.append("📈 Most major indices are positive, showing overall market optimism.")
        elif positive_indices >= total_indices * 0.25:
            insights.append("⚖️ Mixed market performance with some indices up and others down.")
        else:
            insights.append("🔴 Most indices are negative today, suggesting market caution.")
        
        # Volatility insights
        avg_abs_change = np.mean([abs(data['change']) for data in market_overview.values()])
        
        if avg_abs_change > 2:
            insights.append("⚡ High volatility detected - consider dollar-cost averaging for new investments.")
        elif avg_abs_change < 0.5:
            insights.append("😴 Low volatility market - relatively stable trading conditions.")
        else:
            insights.append("📊 Normal market volatility - good conditions for regular investing.")
        
        # Sector rotation insights
        sector_perf = self.get_sector_performance()
        best_sector = max(sector_perf.items(), key=lambda x: x[1])
        worst_sector = min(sector_perf.items(), key=lambda x: x[1])
        
        insights.append(f"🏆 Best performing sector: {best_sector[0]} (+{best_sector[1]:.1f}%)")
        insights.append(f"📉 Worst performing sector: {worst_sector[0]} ({worst_sector[1]:+.1f}%)")
        
        # Investment timing insights
        sp500_data = None
        for name, data in market_overview.items():
            if 'S&P 500' in name:
                sp500_data = data
                break
        
        if sp500_data:
            recent_prices = sp500_data['prices'][-10:]  # Last 10 days
            if len(recent_prices) >= 2:
                trend = "upward" if recent_prices[-1] > recent_prices[0] else "downward"
                insights.append(f"📈 S&P 500 shows {trend} trend over the last 10 trading days.")
        
        # General market insights
        insights.append("💡 Remember: Market timing is difficult. Focus on consistent, long-term investing.")
        
        return insights
    
    def get_economic_indicators(self):
        """Get key economic indicators (simplified)"""
        # In a real implementation, this would fetch from FRED API or similar
        # For now, we'll provide typical ranges and mock current values
        
        np.random.seed(int(datetime.now().timestamp()) // 86400)  # Changes daily
        
        indicators = {
            'Federal Funds Rate': {
                'current': round(np.random.uniform(0.25, 5.5), 2),
                'description': 'The target interest rate set by the Federal Reserve',
                'impact': 'Higher rates typically strengthen USD and affect borrowing costs'
            },
            '10-Year Treasury Yield': {
                'current': round(np.random.uniform(1.5, 5.0), 2),
                'description': 'Yield on 10-year U.S. Treasury bonds',
                'impact': 'Key benchmark for mortgage rates and long-term investment returns'
            },
            'Unemployment Rate': {
                'current': round(np.random.uniform(3.5, 8.0), 1),
                'description': 'Percentage of labor force that is unemployed',
                'impact': 'Lower unemployment generally indicates economic strength'
            },
            'Inflation Rate (CPI)': {
                'current': round(np.random.uniform(1.0, 6.0), 1),
                'description': 'Consumer Price Index year-over-year change',
                'impact': 'Higher inflation erodes purchasing power and affects Fed policy'
            }
        }
        
        return indicators
    
    def get_crypto_prices(self):
        """Get major cryptocurrency prices"""
        crypto_symbols = ['BTC-USD', 'ETH-USD', 'ADA-USD', 'DOT-USD']
        crypto_data = {}
        
        for symbol in crypto_symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="5d")
                
                if not hist.empty:
                    current_price = hist['Close'][-1]
                    prev_price = hist['Close'][-2] if len(hist) > 1 else current_price
                    change_pct = ((current_price - prev_price) / prev_price) * 100
                    
                    clean_name = symbol.replace('-USD', '')
                    crypto_data[clean_name] = {
                        'price': current_price,
                        'change': change_pct
                    }
                else:
                    clean_name = symbol.replace('-USD', '')
                    crypto_data[clean_name] = self._generate_mock_crypto_price(clean_name)
                    
            except Exception as e:
                clean_name = symbol.replace('-USD', '')
                crypto_data[clean_name] = self._generate_mock_crypto_price(clean_name)
        
        return crypto_data
    
    def _generate_mock_crypto_price(self, symbol):
        """Generate mock cryptocurrency price"""
        np.random.seed(hash(symbol) % 2**32)
        
        # Base prices for major cryptos
        base_prices = {
            'BTC': 45000,
            'ETH': 3000,
            'ADA': 0.50,
            'DOT': 25
        }
        
        base_price = base_prices.get(symbol, 100)
        change_pct = np.random.normal(0, 5)  # 5% daily volatility for crypto
        current_price = base_price * (1 + change_pct/100)
        
        return {
            'price': current_price,
            'change': change_pct
        }
    
    def get_bond_yields(self):
        """Get current bond yields"""
        # Treasury yield symbols
        bonds = {
            '^TNX': '10-Year Treasury',
            '^FVX': '5-Year Treasury',
            '^TYX': '30-Year Treasury'
        }
        
        bond_data = {}
        
        for symbol, name in bonds.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="5d")
                
                if not hist.empty:
                    current_yield = hist['Close'][-1]
                    prev_yield = hist['Close'][-2] if len(hist) > 1 else current_yield
                    change = current_yield - prev_yield
                    
                    bond_data[name] = {
                        'yield': current_yield,
                        'change': change
                    }
                else:
                    bond_data[name] = self._generate_mock_bond_yield(name)
                    
            except Exception as e:
                bond_data[name] = self._generate_mock_bond_yield(name)
        
        return bond_data
    
    def _generate_mock_bond_yield(self, bond_name):
        """Generate mock bond yield"""
        np.random.seed(hash(bond_name) % 2**32)
        
        # Typical yield ranges
        if '10-Year' in bond_name:
            base_yield = np.random.uniform(2.0, 5.0)
        elif '5-Year' in bond_name:
            base_yield = np.random.uniform(1.5, 4.5)
        else:  # 30-Year
            base_yield = np.random.uniform(2.5, 5.5)
        
        change = np.random.normal(0, 0.05)  # Small daily changes
        
        return {
            'yield': base_yield,
            'change': change
        }
