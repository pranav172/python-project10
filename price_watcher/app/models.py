import firebase_admin
from firebase_admin import credentials, firestore
from app.utils import get_current_price

# Initialize Firebase
cred = credentials.Certificate('path/to/your/firebase/credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_product(link, level):
    current_price = get_current_price(link)
    if current_price:
        doc_ref = db.collection("products").document()
        doc_ref.set({
            "link": link,
            "price": current_price,
            "level": level
        })
        return True
    return False

def get_all_products():
    products_ref = db.collection("products")
    return products_ref.stream()

def update_product_price(product_id, new_price):
    db.collection("products").document(product_id).update({"price": new_price})