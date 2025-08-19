from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import json , os


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

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
    students = load_students() #variable the student data is loaded into - a dict

    # Check if username already exists
    for s in students:
        if s["username"] == student.username:
            return {"error": "Username already exists"}

    # Convert to dict and save - appending the new data
    students.append(student.model_dump())
    save_students(students)

    return {"message": "Student registered successfully"}