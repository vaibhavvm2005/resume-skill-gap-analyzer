# 🧠 Resume Skill Gap Analyzer

A Machine Learning-powered REST API built with FastAPI that analyzes a user's skills, compares them with industry job role requirements, calculates a skill match percentage, and identifies missing skills to help users prepare for their target careers.

## 🚀 Features

* Analyze skills for multiple job roles
* Calculate skill match percentage
* Identify missing skills
* FastAPI REST API
* Machine Learning with Scikit-learn
* Interactive Swagger UI
* JSON-based request and response

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Joblib
* Uvicorn

## 📌 API Endpoints

| Method | Endpoint   | Description                      |
| ------ | ---------- | -------------------------------- |
| GET    | `/`        | Welcome message                  |
| GET    | `/health`  | API health check                 |
| GET    | `/roles`   | List available job roles         |
| POST   | `/analyze` | Analyze skills and identify gaps |

## ▶️ Run the Project

```bash
git clone https://github.com/vaibhavvm2005/resume-skill-gap-analyzer.git
cd resume-skill-gap-analyzer

python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
# .venv\Scripts\activate

pip install -r requirements.txt

python train_model.py

uvicorn app:app --reload
```

Open your browser and visit:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

## 📄 License

This project is open source and available under the MIT License.
