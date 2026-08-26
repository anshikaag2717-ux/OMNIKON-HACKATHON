from Explain_model import explain_prediction


student = {
    "Age": 20,
    "Family_Income": 30000,
    "Study_Hours_per_Day": 4,
    "Attendance_Rate": 65,
    "Assignment_Delay_Days": 6,
    "Travel_Time_Minutes": 80,
    "Stress_Index": 8,
    "GPA": 5.5,
    "Semester_GPA": 5.8,
    "CGPA": 6.0,

    "Gender": "Male",
    "Internet_Access": "No",
    "Part_Time_Job": "No",
    "Scholarship": "No",
    "Semester": 4,
    "Department": "CS",
    "Parental_Education": "Graduate"
}


result = explain_prediction(student)

print("\nRisk Probability:")
print(result["risk_probability"])

print("\nRisk Level:")
print(result["risk_level"])

print("\nFactors Increasing Risk:")
for factor in result["risk_increasing_factors"]:
    print(factor)

print("\nFactors Reducing Risk:")
for factor in result["risk_reducing_factors"]:
    print(factor)