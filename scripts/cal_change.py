import pandas as pd

def cal_change(current_price):
    df = pd.read_csv('./data/stock_data.csv')
    apple = df[df['Company'] == 'AAPL']
    last_price = apple['Price'].iloc[-1]

    price_diff= current_price - last_price
    percentage_diff = (price_diff / last_price) * 100
    
    print(f"Price difference: {price_diff:.2f}")
    print(f"Percentage difference: {percentage_diff:.2f}%")
    
    return last_price, price_diff, percentage_diff
