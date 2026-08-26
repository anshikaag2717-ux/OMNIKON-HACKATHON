from src.student_risk import assess_student


student = {
    "Age": 20,
    "Family_Income": 30000,
    "Study_Hours_per_Day": 4,
    "Attendance_Rate": 65,
    "Assignment_Delay_Days": 6,
    "Travel_Time_Minutes": 80,
    "Stress_Index": 8,
    "GPA": 1.5,
    "Semester_GPA": 1.8,
    "CGPA": 2.0,

    "Gender": "Male",
    "Internet_Access": "No",
    "Part_Time_Job": "No",
    "Scholarship": "No",
    "Semester": 4,
    "Department": "CS",
    "Parental_Education": "Graduate"
}


result = assess_student(student)


print("\n==============================")
print("     STUDENT RISK ASSESSMENT")
print("==============================")

print(f"\nRisk Probability : {result['risk_probability']}")
print(f"Risk Percentage  : {result['risk_percentage']}%")
print(f"Risk Level       : {result['risk_level']}")


print("\nRisk Factors:")

for factor in result["risk_factors"]:
    print(
        f"- {factor['factor']} "
        f"({factor['importance']})"
    )


print("\nRisk Reducing Factors:")

for factor in result["risk_reducing_factors"]:
    print(
        f"- {factor['factor']} "
        f"({factor['importance']})"
    )


print("\nRecommendations:")

for recommendation in result["recommendations"]:
    print(
        f"\n[{recommendation['priority']}] "
        f"{recommendation['title']}"
    )

    print(f"  Factor: {recommendation['factor']}")
    print(f"  Action: {recommendation['description']}")