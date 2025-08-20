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

# Pydantic model for job applications
class JobApplication(BaseModel):
    job_title: str
    company: str
    date_applied: str   # keeping it as string for simplicity
    status: str
