from fastapi import FastAPI, Depends
from pydantic import BaseModel
from pathlib import Path
import json


from auth import get_current_user

app = FastAPI()

# Path to applications.json
APPLICATIONS_FILE = Path("applications.json")

# Helper functions
def load_applications():
    if APPLICATIONS_FILE.exists():
        with open(APPLICATIONS_FILE, "r") as f:
            return json.load(f)
    return []

def save_applications(applications):
    with open(APPLICATIONS_FILE, "w") as f:
        json.dump(applications, f, indent=4)


class JobApplication(BaseModel):
    job_title: str
    company: str
    date_applied: str   # keeping it as string for simplicity
    status: str


@app.post("/applications/")
def add_application(application: JobApplication, user: dict = Depends(get_current_user)):
    applications = load_applications()
    new_entry = {
        "username": user["username"],
        "job_title": application.job_title,
        "company": application.company,
        "date_applied": application.date_applied,
        "status": application.status,
    }
    applications.append(new_entry)
    save_applications(applications)
    return {"message": "Application added successfully", "application": new_entry}


@app.get("/applications/")
def view_applications(user: dict = Depends(get_current_user)):
    applications = load_applications()
    user_apps = [app for app in applications if app["username"] == user["username"]]
    return {"username": user["username"], "applications": user_apps}
