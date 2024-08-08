import requests
from bs4 import BeautifulSoup

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