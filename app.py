# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from pydantic import BaseModel
import pandas as pd

# Create FastAPI app
app = FastAPI(title="Resume Skill Gap Analyzer API")

# Load dataset
df = pd.read_csv("data/skills.csv")

# Request model
class ResumeRequest(BaseModel):
    role: str
    skills: list[str]


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Resume Skill Gap Analyzer API"
    }


# Health check
@app.get("/health")
def health():
    return {
        "status": "API is running"
    }


# Get all available roles
@app.get("/roles")
def get_roles():
    return {
        "roles": df["Role"].tolist()
    }


# Analyze skills
@app.post("/analyze")
def analyze(request: ResumeRequest):

    # Find the selected role
    role_data = df[df["Role"].str.lower() == request.role.lower()]

    if role_data.empty:
        return {
            "error": "Role not found"
        }

    # Convert role skills into a list
    required_skills = [
        skill.strip()
        for skill in role_data.iloc[0]["Skills"].split(",")
    ]

    # User skills
    user_skills = [skill.strip() for skill in request.skills]

    # Missing skills
    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in [s.lower() for s in user_skills]
    ]

    # Match percentage
    matched = len(required_skills) - len(missing_skills)

    match_percentage = round(
        (matched / len(required_skills)) * 100,
        2
    )

    return {
        "Role": request.role,
        "Match Percentage": match_percentage,
        "Missing Skills": missing_skills
    }