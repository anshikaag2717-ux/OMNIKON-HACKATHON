from fastapi import FastAPI
from pydantic import BaseModel

from pathlib import Path
import sys


# ============================================================
# PROJECT PATHS
# ============================================================

# Project root = ML/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ML/src/
SRC_PATH = PROJECT_ROOT / "src"

# Allow Python to import files from src/
sys.path.insert(0, str(SRC_PATH))


# ============================================================
# IMPORT ML PIPELINE
# ============================================================

from student_risk import assess_student


# ============================================================
# CREATE FASTAPI APP
# ============================================================

app = FastAPI(
    title="Student Dropout Risk API",
    description="API for predicting student dropout risk",
    version="1.0.0"
)


# ============================================================
# STUDENT INPUT SCHEMA
# ============================================================

class StudentData(BaseModel):

    Age: int

    Gender: str
    Department: str
    Semester: str

    CGPA: float
    GPA: float
    Semester_GPA: float

    Attendance_Rate: float
    Study_Hours_per_Day: float
    Assignment_Delay_Days: float
    Travel_Time_Minutes: float

    Family_Income: float
    Stress_Index: float

    Parental_Education: str
    Internet_Access: str
    Scholarship: str
    Part_Time_Job: str


# ============================================================
# ROOT / HEALTH CHECK
# ============================================================

@app.get("/")
def root():

    return {
        "message": "Student Dropout Risk API is running",
        "status": "healthy"
    }


# ============================================================
# PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict_student(student: StudentData):

    # Convert Pydantic model into normal Python dictionary
    student_data = student.model_dump()

    # Run complete ML pipeline
    result = assess_student(student_data)

    # Return prediction + explanation + recommendations
    return result