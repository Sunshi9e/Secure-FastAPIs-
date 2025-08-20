from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import json, os

from auth import authenticate_user, create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI()

NOTES_FILE = "notes.json"

# Ensure file exists
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as f:
        json.dump({}, f)

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str

class Note(BaseModel):
    title: str
    content: str
    date: str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# Utility functions
def read_notes():
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def write_notes(data):
    with open(NOTES_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Login endpoint
@app.post("/login/", response_model=Token)
def login(form_data: LoginRequest):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=None
    )
    return {"access_token": token, "token_type": "bearer"}

# Add a note
@app.post("/notes/")
def add_note(note: Note, current_user: dict = Depends(get_current_user)):
    notes = read_notes()
    user_notes = notes.get(current_user["username"], [])
    user_notes.append(note.dict())
    notes[current_user["username"]] = user_notes
    write_notes(notes)
    return {"message": "Note added successfully", "note": note}

# View notes
@app.get("/notes/", response_model=List[Note])
def get_notes(current_user: dict = Depends(get_current_user)):
    notes = read_notes()
    return notes.get(current_user["username"], [])
