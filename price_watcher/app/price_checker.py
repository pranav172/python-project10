import requests
from bs4 import BeautifulSoup
from app.models import get_all_products, update_product_price
from app import scheduler

def parse_price(price_str):
    price_str = price_str.strip()[4:]
    price_str = price_str.replace(',', '')
    return float(price_str)

def get_current_price(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.find("span", {"id": "ProductPrice-8167267041531"})
        if price_element:
            return parse_price(price_element.get_text(strip=True))
    except Exception as e:
        print(f"Error fetching price: {e}")
    return None
from app import scheduler
from app.utils import get_current_price
from app.models import get_all_products, update_product_price

def check_prices():
    products = get_all_products()
    for product in products:
        product_data = product.to_dict()
        current_price = get_current_price(product_data['link'])
        if current_price and current_price != product_data['price']:
            update_product_price(product.id, current_price)
            send_email_notification(product_data['link'], product_data['price'], current_price, product_data['level'])

def send_email_notification(link, old_price, new_price, level):
    # Implement email sending logic here
    print(f"Price changed for {link}: Old price: {old_price}, New price: {new_price}, Level: {level}")

@scheduler.task('cron', id='daily_price_check', hour=10)
def scheduled_check():
    with scheduler.app.app_context():
        check_prices()