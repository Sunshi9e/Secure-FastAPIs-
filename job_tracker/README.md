# Job Application Tracker API (FastAPI)

A beginner-friendly FastAPI project that demonstrates **per-user secure access**.  
- Each user can only add and view **their own job applications**.  
- Applications are saved in a local JSON file (`applications.json`).  
- Authentication is simulated with simple tokens (no database or JWT yet).  

---

## 📂 Project Structure

```
job_tracker/
│
├── main.py # FastAPI app (endpoints)
├── auth.py # Authentication & current user dependency
├── applications.json # Stores job applications
```

---

## ⚙️ Installation & Setup

### 1. Create project folder

```bash
mkdir job_tracker
cd job_tracker
```
### 2. Install dependencies

```bash
pip install fastapi uvicorn
```
### 3. Create files

- `applications.json` → put [] inside

- `auth.py` → contains fake authentication (tokens)

- `main.py` → contains API endpoints

### 4. Run the server

```bash 
uvicorn main:app --reload
```
**Server runs at:**
👉 `http://127.0.0.1:8000`

**Swagger docs:**
👉 `http://127.0.0.1:8000/docs`

---

## 🔑 Authentication

This project uses fake tokens defined in `auth.py`:

```json
fake_users_db = {
    "admin_token": {"username": "admin", "role": "admin"},
    "user1_token": {"username": "alice", "role": "user"},
    "user2_token": {"username": "bob", "role": "user"},
}
```
### Use tokens in headers:
```makefile
Authorization: Bearer user1_token
```
**OR**
```makefile
Authorization: Bearer user2_token
```
---

##  Endpoints

### 1. Add a Job Application

```http
POST /applications/
```
**Headers:**
```makefile
Authorization: Bearer user1_token
```
**Body(JSON)**
```json
{
  "job_title": "Backend Developer",
  "company": "TechCorp",
  "date_applied": "2025-08-20",
  "status": "Pending"
}
```
**Response:**
```json
{
  "message": "Application added successfully",
  "application": {
    "username": "alice",
    "job_title": "Backend Developer",
    "company": "TechCorp",
    "date_applied": "2025-08-20",
    "status": "Pending"
  }
}
```
### 2. View Your Applications

```h
GET /applications/
```
**Headers:**

```makefile
Authorization: Bearer user1_token
```
**Response:**

```json
{
  "username": "alice",
  "applications": [
    {
      "username": "alice",
      "job_title": "Backend Developer",
      "company": "TechCorp",
      "date_applied": "2025-08-20",
      "status": "Pending"
    }
  ]
}
```
---

## 📌 Future Improvements

- Replace fake tokens with **JWT authentication**

- Add **update/delete** endpoints for applications

- Store data in a real database (SQLite, PostgreSQL, etc.)