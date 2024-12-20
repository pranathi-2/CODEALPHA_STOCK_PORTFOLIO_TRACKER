import yfinance as yf
import pandas as pd
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    def add_stock(self, symbol, shares, purchase_price):
        if symbol in self.portfolio:
            print(f"{symbol} is already in the portfolio.")
        else:
            self.portfolio[symbol] = {'shares': shares, 'purchase_price': purchase_price}
            print(f"Added {shares} shares of {symbol} at ${purchase_price} each.")
    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"Removed {symbol} from the portfolio.")
        else:
            print(f"{symbol} is not in the portfolio.")
    def get_current_price(self, symbol):
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        return data['Close'][0]
    def track_performance(self):
        total_value = 0
        total_investment = 0
        for symbol, details in self.portfolio.items():
            current_price = self.get_current_price(symbol)
            total_value += current_price * details['shares']
            total_investment += details['shares'] * details['purchase_price']
            print(f"{symbol}: {details['shares']} shares, Purchase Price: ${details['purchase_price']},"f"Current Price: ${current_price}, Current Value: ${current_price * details['shares']}")
        portfolio_return = total_value - total_investment
        print("\nPortfolio Performance:")
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"Total Current Value: ${total_value:.2f}")
        print(f"Total Return: ${portfolio_return:.2f}")
        print(f"Portfolio Return Percentage: {100 * (portfolio_return / total_investment) if total_investment != 0 else 0:.2f}%")
    def portfolio_summary(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
        else:
            print("\nPortfolio Summary:")
            for symbol, details in self.portfolio.items():
                print(f"{symbol}: {details['shares']} shares at ${details['purchase_price']} each")
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10, 150)
portfolio.add_stock('GOOGL', 5, 2500)
portfolio.track_performance()
portfolio.portfolio_summary()
portfolio.remove_stock('AAPL')
portfolio.track_performance()
portfolio.portfolio_summary()
