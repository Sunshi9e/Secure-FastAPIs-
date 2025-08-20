# 📒 Notes API with JWT Authentication

A simple FastAPI project where users can log in, get a JWT token, and manage their personal notes.
Each user only sees their own notes.

## Features

- **JWT Authentication**

    - `POST /login/` returns a token.

- **Notes Management**

    - `POST /notes/` → Add a note (requires token).

    - `GET /notes/` → View your notes only.

- **Data Storage**

    - Notes saved in `notes.json` file.

    - Notes are tied to each username.

---
## Project Structure

```bash
notes_api/
│── main.py          # FastAPI app with endpoints
│── auth.py          # Authentication & JWT helper functions
│── notes.json       # Stores notes data
│── requirements.txt # Dependencies
│── README.md        # Project documentation

```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone or download project

```bash
git clone https://github.com/yourusername/notes_api.git
cd notes_api
```
### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the server

```bash
uvicorn main:app --reload
```
Server will start at 👉 `http://127.0.0.1:8000`

---

## 🔑 Authentication Flow

### 1. Login to get a token

- Endpoint: POST /login/

- Example body:

    ```json
        {
            "username": "alice",
            "password": "password"
        }

    ```
        
- **Response:**

    ```json
        {
            "access_token": "your.jwt.token",
            "token_type": "bearer"
        }
    ```

### Use token for secure routes

- Add header in Postman:

    ```makefile

    Authorization: Bearer your.jwt.token

    ```
## Endpoints
🔹 `POST /login/`

- Logs in a user and returns a JWT token.

🔹 `POST /notes/`

- equires JWT token.

- Adds a new note for the logged-in user.

- Example body: 

    ```json
    {

        "title": "First Note",
        "content": "Learning FastAPI!",
        "date": "2025-08-20"
    }

    ```
🔹 `GET /notes/`

- Requires JWT token.

- Returns all notes that belong to the logged-in user.

---

## Data Example (notes.json)

```json
[
  {
    "username": "alice",
    "title": "First Note",
    "content": "Learning FastAPI!",
    "date": "2025-08-20"
  },
  {
    "username": "bob",
    "title": "Shopping List",
    "content": "Milk, Bread, Eggs",
    "date": "2025-08-21"
  }
]
```
---

## Summary

- Users log in and get tokens 🔑

- Tokens protect endpoints 🔒

- Each user manages their own notes only 📝

- Notes stored persistently in `notes.json`

## 🔮 Future Improvements

- Add user registration endpoint (instead of hardcoded users).

- Enable password hashing for stronger security.

- Add note editing and deletion endpoints.

- Implement refresh tokens for longer sessions.

- Switch to a database (SQLite/Postgres) instead of `notes.json`.

- Add pagination & search for large note collections.
