from scripts.scrap_price import scrap_price
from scripts.cal_change import cal_change
from scripts.email_alert import email_alert

def main():    
    try:
        current_price = scrap_price()
        last_price, price_diff, percentage_diff = cal_change(current_price)
        threshold = 50
        if abs(price_diff) > threshold:
            email_alert(current_price, last_price, price_diff, percentage_diff)
            
    except Exception as e:
            print(f"An error occurred: {e}")
            
if __name__ == '__main__':
    main()