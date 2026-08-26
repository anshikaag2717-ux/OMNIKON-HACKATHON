import joblib
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "dropout_model.joblib"

model = joblib.load(MODEL_PATH)


def get_risk_factors(student_data):

    factors = []

    # GPA
    if student_data["GPA"] < 1.55:
        factors.append("Very low GPA")
    elif student_data["GPA"] < 2.35:
        factors.append("Below-median GPA")

    # Stress
    if student_data["Stress_Index"] >= 6.7:
        factors.append("High stress level")

    # Attendance
    if student_data["Attendance_Rate"] < 76.4:
        factors.append("Low attendance")

    # Assignment delays
    if student_data["Assignment_Delay_Days"] > 3:
        factors.append("Frequent assignment delays")

    # Travel time
    if student_data["Travel_Time_Minutes"] >= 60:
        factors.append("Long travel time")

    # Internet access
    if student_data["Internet_Access"] == "No":
        factors.append("No internet access")

    return factors


def explain_student(student_data):
    """
    Generate dropout risk prediction and
    student-specific risk factors.
    """

    student_df = pd.DataFrame([student_data])

    # Get dropout probability
    probability = model.predict_proba(student_df)[0, 1]

    # Determine risk level
    if probability >= 0.60:
        risk_level = "High"
    elif probability >= 0.40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # Determine risk factors
    risk_factors = get_risk_factors(student_data)

    return {
        "risk_probability": round(float(probability), 4),
        "risk_level": risk_level,
        "risk_factors": risk_factors
    }