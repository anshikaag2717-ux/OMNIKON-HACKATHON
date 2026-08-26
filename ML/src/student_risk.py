from predict import predict_dropout
from Explain_model import explain_prediction
from recommendation import generate_recommendations


def assess_student(student_data):
    """
    Complete student dropout-risk assessment.

    Combines:
    1. ML prediction
    2. Model explanation
    3. Intervention recommendations
    """

    # -----------------------------
    # 1. Get prediction
    # -----------------------------
    prediction = predict_dropout(student_data)

    risk_probability = prediction["risk_probability"]
    risk_level = prediction["risk_level"]

    # -----------------------------
    # 2. Explain prediction
    # -----------------------------
    explanation = explain_prediction(student_data)

    risk_factors = explanation["risk_increasing_factors"]

    risk_reducing_factors = explanation["risk_reducing_factors"]

    # -----------------------------
    # 3. Generate recommendations
    # -----------------------------
    recommendations = generate_recommendations(
        risk_level,
        risk_factors
    )

    # -----------------------------
    # 4. Return complete result
    # -----------------------------
    return {
        "risk_probability": risk_probability,
        "risk_percentage": round(risk_probability * 100, 2),
        "risk_level": risk_level,

        "risk_factors": risk_factors,

        "risk_reducing_factors": risk_reducing_factors,

        "recommendations": recommendations
    }