# 🛒 Secure Shopping Cart API (FastAPI)

A beginner-friendly FastAPI project that demonstrates **role-based access control** using simple token authentication.  
- Admins can add products  
- Anyone can view products  
- Authenticated users can add products to their cart  
- Users can view their own cart  

Data is saved locally in JSON files (`products.json`, `cart.json`).  
No database required — perfect for beginners learning FastAPI.

---

## 📂 Project Structure
```
shopping_api/
│
├── main.py # Main FastAPI app (endpoints)
├── auth.py # Authentication & role checking
├── products.json # Stores products
├── cart.json # Stores shopping carts
```

---

## ⚙️ Installation & Setup

### 1. Clone the project or create the folder
```bash
mkdir shopping_api
cd shopping_api
```
### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Create required files

- products.json → put []

- cart.json → put []

### 4. Run the server

```bash
uvicorn main:app --reload
```
**Server runs at:**
👉 `http://127.0.0.1:8000`

**Swagger UI docs:**
👉 `http://127.0.0.1:8000/docs`

## 🔑 Authentication

This project uses fake tokens (no real JWT yet).

Available tokens in `auth.py`:

```json
fake_users_db = {
    "admin_token": {"username": "admin", "role": "admin"},
    "customer_token": {"username": "john", "role": "customer"},
}
```

### Use them in headers:

```makefile
Authorization: Bearer admin_token
```
**OR**

```makefile
Authorization: Bearer customer_token
```

## Endpoints

### 1. Public – View Products

```http
GET /products/
```
- No token required

- Returns list of products

### 2. Admin Only – Add Product

```http
POST /admin/add_product/
```

**Headers:**
```makefile
Authorization: Bearer admin_token
```

**Body (JSON):**

```json
{
  "name": "Laptop",
  "price": 1200.50
}
```

### 3. Authenticated – Add to Cart

```http
POST /cart/add/
```
**Headers:**

```makefile
Authorization: Bearer customer_token
```
**Body (JSON):**

```json
{
  "product_name": "Laptop",
  "quantity": 2
}
```
### 4. Authenticated – View Cart

```http
GET /cart/
```

**Headers:**

```makefile
Authorization: Bearer customer_token
```
Returns only the items belonging to that user.

## Future Improvements

- Replace fake tokens with JWT authentication

- Use a real database (SQLite, PostgreSQL, etc.) instead of JSON files

- Add more features (remove items, checkout, etc.)

