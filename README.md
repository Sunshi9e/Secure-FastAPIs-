# Secure Student Portal API

A simple **FastAPI** project where students can:

- Register with a username, password, and grades

- Log in with their credentials

- View their grades (protected by authentication)

Passwords are stored securely (hashed) using `passlib`.
Data is saved locally in `students.json`.

## Features

- **Register a student →** /register/

- **Login and get a token →** /login/

- **View grades (requires token) →** /grades/

- **Passwords are hashed (not stored in plain text)**

- **File operations are wrapped with try/except for safety**

## Setup Instructions
1. Clone this Repository
```bash
git clone https://github.com/vivixell/secure-fastapis-.git
cd student-portal
```
2. Create Virtual Environment & Install Dependencies (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install fastapi uvicorn passlib[bcrypt]
```
3. Run the App
```python
uvicorn main:app --reload
```

## API Endpoints

1. Register Student

**POST** `/register/`
Example JSON body:

```json
{
  "username": "john",
  "password": "mypassword",
  "grades": [90, 85, 100]
}
```
2. **Login**

**POST** `/login/`
Example JSON body:

```json
{
  "username": "john",
  "password": "mypassword",
  "grades": []
}
```
The `grade` is optional here. 
Response:

```json
{
  "access_token": "john",
  "token_type": "bearer"
}
```

3. **View Grades (Protected)**

**GET** `/grades/`

Requires an Authorization header:
```makefile
Authorization: Bearer john
```
Response:
```json
{
  "grades": [90, 85, 100]
}
```
## Testing with Postman

**Register →** `/register/`

**Login →** `/login/` → **copy access_token**

**Call** `/grades/` with header:
```makefile
Authorization: Bearer <token>
```
