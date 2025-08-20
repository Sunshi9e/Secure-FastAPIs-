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