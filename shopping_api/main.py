from fastapi import FastAPI, Depends
import json
from pathlib import Path
from pydantic import BaseModel

# import dependencies from auth.py
from auth import require_admin

app = FastAPI()

# Path to products.json
PRODUCTS_FILE = Path("products.json")

# Helper function 
def load_products():
    if PRODUCTS_FILE.exists():
        with open(PRODUCTS_FILE, "r") as f:
            return json.load(f)
    return []

# Helper function 
def save_products(products):
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products, f, indent=4)


class Product(BaseModel):
    name: str
    price: float


@app.get("/products/")
def get_products():
    products = load_products()
    return {"products": products}

# Admin endpoint: add new product
@app.post("/admin/add_product/")
def add_product(product: Product, user: dict = Depends(require_admin)):
    products = load_products()
    products.append(product.model_dump())  # convert to dict
    save_products(products)
    return {"message": "Product added successfully", "product": product}


# Path to cart.json
CART_FILE = Path("cart.json")


def load_cart():
    if CART_FILE.exists():
        with open(CART_FILE, "r") as f:
            return json.load(f)
    return []


def save_cart(cart):
    with open(CART_FILE, "w") as f:
        json.dump(cart, f, indent=4)

# model for CartItem
class CartItem(BaseModel):
    product_name: str
    quantity: int

# Endpoint: Add item to cart (any authenticated user)
from auth import get_current_user

@app.post("/cart/add/")
def add_to_cart(item: CartItem, user: dict = Depends(get_current_user)):
    cart = load_cart()

    # Check if product exists
    products = load_products()
    product_names = [p["name"] for p in products]
    if item.product_name not in product_names:
        return {"error": "Product does not exist"}

    # Add to cart
    cart_entry = {
        "username": user["username"],
        "product_name": item.product_name,
        "quantity": item.quantity,
    }
    cart.append(cart_entry)
    save_cart(cart)

    return {"message": "Item added to cart", "cart_item": cart_entry}

@app.get("/cart/")
def view_cart(user: dict = Depends(get_current_user)):
    cart = load_cart()
    # Filter only items belonging to this user
    user_cart = [item for item in cart if item["username"] == user["username"]]
    return {"username": user["username"], "cart": user_cart}
