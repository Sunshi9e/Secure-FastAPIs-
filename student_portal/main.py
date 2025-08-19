from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext
import json , os


app = FastAPI()
auth = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Student model
class Student(BaseModel):
    username: str
    password: str
    grades: list[int] = []

# File to store students
STUDENTS_FILE = "students.json"

# function to read students.json
def load_students():
    try:
        if not os.path.exists(STUDENTS_FILE):
            return []
        with open(STUDENTS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []
    

# function to save students.json
def save_students(students):
    try:
        with open(STUDENTS_FILE, "w") as f:
            json.dump(students, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)


# Register endpoint
@app.post("/register/")
def register(student: Student):
    students = load_students()

    for s in students:
        if s["username"] == student.username:
            return {"error": "Username already exists"}

    # Hash the password before saving
    hashed = hash_password(student.password)
    student.password = hashed

    students.append(student.model_dump())
    save_students(students)

    return {"message": "Student registered successfully"}



# Login endpoint

@app.post("/login/")
def login(student: Student):
    students = load_students()

    for s in students:
        if s["username"] == student.username:
            if verify_password(student.password, s["password"]):
            
                return {"access_token": student.username, "token_type": "bearer"}
            return {"error": "Invalid password"}

    return {"error": "Invalid username"}


@app.get("/grades/")
def get_grades(token: str = Depends(auth)):
    students = load_students()

    # token is just username for now
    for s in students:
        if s["username"] == token:
            return {"grades": s["grades"]}

    return {"error": "Invalid token"}

