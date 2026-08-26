def generate_recommendations(
    risk_level,
    risk_increasing_factors
):
    """
    Generate intervention recommendations based on
    overall risk level and model-identified risk factors.

    Parameters
    ----------
    risk_level : str
        "Low", "Medium", or "High"

    risk_increasing_factors : list
        Risk factors returned by explain_model.py.

    Returns
    -------
    list
        Recommended interventions.
    """

    recommendations = []

    # --------------------------------------------------
    # Risk-level guidance
    # --------------------------------------------------

    if risk_level == "High":
        default_priority = "High"

    elif risk_level == "Medium":
        default_priority = "Medium"

    else:
        default_priority = "Low"


    # --------------------------------------------------
    # Recommendation rules
    # --------------------------------------------------

    recommendation_rules = {

        "GPA": {
            "type": "academic_support",
            "title": "Academic mentoring",
            "description": (
                "Provide targeted academic mentoring and "
                "subject-specific support."
            )
        },

        "Semester GPA": {
            "type": "academic_support",
            "title": "Academic performance monitoring",
            "description": (
                "Monitor recent academic performance and "
                "provide additional study support."
            )
        },

        "Attendance": {
            "type": "attendance",
            "title": "Attendance intervention",
            "description": (
                "Follow up with the student to identify "
                "barriers to regular attendance."
            )
        },

        "Stress level": {
            "type": "wellbeing",
            "title": "Wellbeing support",
            "description": (
                "Recommend appropriate counselling or "
                "student wellbeing resources."
            )
        },

        "Assignment delays": {
            "type": "academic_support",
            "title": "Academic planning support",
            "description": (
                "Provide time-management and study-planning "
                "support to improve assignment completion."
            )
        },

        "Travel time": {
            "type": "logistical_support",
            "title": "Travel-related support",
            "description": (
                "Consider flexible academic support or "
                "scheduling options to reduce the impact of travel."
            )
        },

        "No internet access": {
            "type": "infrastructure_support",
            "title": "Connectivity support",
            "description": (
                "Provide access to campus internet or "
                "alternative learning resources."
            )
        }
    }


    # --------------------------------------------------
    # Generate recommendations from model factors
    # --------------------------------------------------

    for factor in risk_increasing_factors:

        factor_name = factor["factor"]

        if factor_name not in recommendation_rules:
            continue

        rule = recommendation_rules[factor_name]

        # Strong model contribution gets higher priority.
        importance = factor.get("importance", "weak")

        if risk_level == "High":
            if importance == "strong":
                priority = "Critical"
            elif importance == "moderate":
                priority = "High"
            else:
                priority = "Medium"

        elif risk_level == "Medium":
            if importance == "strong":
                priority = "High"
            elif importance == "moderate":
                priority = "Medium"
            else:
                priority = "Low"

        else:
            # Low-risk students should generally be monitored
            # rather than immediately escalated.
            if importance == "strong":
                priority = "Medium"
            else:
                priority = "Low"

        recommendations.append({
            "type": rule["type"],
            "factor": factor_name,
            "title": rule["title"],
            "description": rule["description"],
            "priority": priority
        })


    # --------------------------------------------------
    # Sort recommendations by priority
    # --------------------------------------------------

    priority_order = {
        "Critical": 0,
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    recommendations.sort(
        key=lambda x: priority_order[x["priority"]]
    )

    return recommendations