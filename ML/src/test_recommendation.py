from recommendation import generate_recommendations


risk_level = "High"

risk_factors = [
    {
        "factor": "GPA",
        "effect": "increases risk",
        "importance": "strong"
    },
    {
        "factor": "Attendance",
        "effect": "increases risk",
        "importance": "moderate"
    },
    {
        "factor": "Stress level",
        "effect": "increases risk",
        "importance": "moderate"
    },
    {
        "factor": "Assignment delays",
        "effect": "increases risk",
        "importance": "moderate"
    },
    {
        "factor": "No internet access",
        "effect": "increases risk",
        "importance": "weak"
    }
]


recommendations = generate_recommendations(
    risk_level,
    risk_factors
)


print("\n==============================")
print("      RECOMMENDATIONS")
print("==============================")


for recommendation in recommendations:

    print(f"\nPriority : {recommendation['priority']}")
    print(f"Type     : {recommendation['type']}")
    print(f"Factor   : {recommendation['factor']}")
    print(f"Title    : {recommendation['title']}")
    print(f"Action   : {recommendation['description']}")