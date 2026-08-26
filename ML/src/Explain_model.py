import joblib
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "dropout_model.joblib"

model = joblib.load(MODEL_PATH)


FEATURE_LABELS = {
    "numerical__GPA": "GPA",
    "numerical__Stress_Index": "Stress level",
    "numerical__Attendance_Rate": "Attendance",
    "numerical__Assignment_Delay_Days": "Assignment delays",
    "numerical__Travel_Time_Minutes": "Travel time",
    "numerical__Semester_GPA": "Semester GPA",

    "categorical__Internet_Access_No": "No internet access",
    "categorical__Internet_Access_Yes": "Internet access",
    "categorical__Part_Time_Job_No": "No part-time job",
    "categorical__Part_Time_Job_Yes": "Part-time job",
    "categorical__Department_CS": "Computer Science department",
    "categorical__Department_Science": "Science department",
    "categorical__Department_Arts": "Arts department",
    "categorical__Gender_Male": "Male",
    "categorical__Scholarship_Yes": "Scholarship",
    "categorical__Scholarship_No": "No scholarship",
    "categorical__Parental_Education_Master" : "Master's parental education",
}


def get_importance(contribution):

    magnitude = abs(contribution)

    if magnitude >= 1.0:
        return "strong"

    elif magnitude >= 0.3:
        return "moderate"

    else:
        return "weak"


def explain_prediction(student_data, top_n=5):

    student_df = pd.DataFrame([student_data])

    preprocessor = model.named_steps["preprocessor"]
    classifier = model.named_steps["classifier"]

    transformed_student = preprocessor.transform(student_df)

    feature_names = preprocessor.get_feature_names_out()

    coefficients = classifier.coef_[0]

    contributions = transformed_student[0] * coefficients

    explanation = pd.DataFrame({
        "Feature": feature_names,
        "Contribution": contributions
    })

    explanation["Contribution"] = (
        explanation["Contribution"].astype(float)
    )

    explanation["Absolute_Contribution"] = (
        explanation["Contribution"].abs()
    )

    explanation = explanation.sort_values(
        "Absolute_Contribution",
        ascending=False
    )

    positive = explanation[
        explanation["Contribution"] > 0
    ].head(top_n)

    negative = explanation[
        explanation["Contribution"] < 0
    ].sort_values(
        "Contribution"
    ).head(top_n)

    probability = model.predict_proba(
        student_df
    )[0, 1]

    if probability >= 0.60:
        risk_level = "High"

    elif probability >= 0.40:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    risk_increasing = []

    for _, row in positive.iterrows():

        feature = row["Feature"]

        label = FEATURE_LABELS.get(
            feature,
            feature
        )

        risk_increasing.append({
            "factor": label,
            "effect": "increases risk",
            "importance": get_importance(
                row["Contribution"]
            )
        })

    risk_reducing = []

    for _, row in negative.iterrows():

        feature = row["Feature"]

        label = FEATURE_LABELS.get(
            feature,
            feature
        )

        risk_reducing.append({
            "factor": label,
            "effect": "reduces risk",
            "importance": get_importance(
                row["Contribution"]
            )
        })

    return {
        "risk_probability": round(
            float(probability),
            4
        ),

        "risk_level": risk_level,

        "risk_increasing_factors": risk_increasing,

        "risk_reducing_factors": risk_reducing
    }