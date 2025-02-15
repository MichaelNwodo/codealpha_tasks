

import time
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty portfolio
portfolio = {}


def fetch_real_time_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='5d')  # Fetch last 5 days of data
        if data.empty:
            print(f'Error: No data found for {symbol}.')
            return None
        return data
    except Exception as e:
        print(f'Error fetching data for {symbol}: {e}')
        return None


def add_stock(symbol, shares):
    data = fetch_real_time_stock_data(symbol)
    if data is not None and not data.empty:
        close_price = float(data['Close'].iloc[-1])
        portfolio[symbol] = {'shares': shares, 'price': close_price}
        print(f'Added {shares} shares of {symbol} at ${close_price:.2f} each.')
    else:
        print(f'Error retrieving data for {symbol}. Please check the stock symbol.')


def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f'Removed {symbol} from portfolio.')
    else:
        print(f'{symbol} not found in portfolio.')


def display_portfolio():
    if portfolio:
        df = pd.DataFrame(portfolio).T
        df['total_value'] = df['shares'] * df['price']
        print(df)
    else:
        print('Portfolio is empty.')


def calculate_portfolio_metrics(symbol):
    df = fetch_real_time_stock_data(symbol)
    if df is not None and not df.empty:
        df['Daily Return'] = df['Close'].pct_change()
        return df
    else:
        print(f'No data available to calculate metrics for {symbol}.')
        return None


def plot_stock_trends(symbol):
    df = fetch_real_time_stock_data(symbol)
    if df is not None and not df.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df['Close'], label=symbol, color='blue')
        plt.title(f'{symbol} Stock Trend')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.legend()
        plt.grid()
        plt.show()
    else:
        print(f'No data available to plot trends for {symbol}.')


def menu():
    while True:
        print('\nStock Portfolio Manager')
        print('1. Add Stock')
        print('2. Remove Stock')
        print('3. Display Portfolio')
        print('4. View Stock Performance')
        print('5. Plot Stock Trends')
        print('6. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            symbol = input('Enter stock symbol: ').upper()
            try:
                shares = int(input('Enter number of shares: '))
                if shares <= 0:
                    print('Error: Number of shares must be positive.')
                else:
                    add_stock(symbol, shares)
            except ValueError:
                print('Error: Please enter a valid integer for shares.')
        elif choice == '2':
            symbol = input('Enter stock symbol to remove: ').upper()
            remove_stock(symbol)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            symbol = input('Enter stock symbol: ').upper()
            df = calculate_portfolio_metrics(symbol)
            if df is not None:
                print(df[['Close', 'Daily Return']].tail())
        elif choice == '5':
            symbol = input('Enter stock symbol: ').upper()
            plot_stock_trends(symbol)
        elif choice == '6':
            print('Exiting program.')
            break
        else:
            print('Invalid choice. Please try again.')


# Run the menu
menu()
