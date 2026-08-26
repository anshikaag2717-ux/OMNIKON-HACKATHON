import joblib
import pandas as pd
from pathlib import Path


# Find the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "dropout_model.joblib"


# Load trained model
model = joblib.load(MODEL_PATH)


def predict_dropout(student_data):
    """
    Predict dropout risk for one student.

    Parameters
    ----------
    student_data : dict
        Student information using the same feature names
        used during model training.

    Returns
    -------
    dict
        Dropout probability, percentage, and risk level.
    """

    student_df = pd.DataFrame([student_data])

    # Predict probability
    probability = model.predict_proba(student_df)[0, 1]

    # Convert probability to percentage
    risk_percentage = round(float(probability) * 100, 2)

    # Determine risk level
    if probability >= 0.60:
        risk_level = "High"

    elif probability >= 0.40:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    return {
        "risk_probability": round(float(probability), 4),
        "risk_percentage": risk_percentage,
        "risk_level": risk_level
    }