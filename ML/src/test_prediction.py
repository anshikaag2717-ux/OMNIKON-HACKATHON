from predict import predict_dropout


student = {
    "Age": 20,
    "Family_Income": 30000,
    "Study_Hours_per_Day": 4,
    "Attendance_Rate": 75,
    "Assignment_Delay_Days": 3,
    "Travel_Time_Minutes": 45,
    "Stress_Index": 6,
    "GPA": 6.8,
    "Semester_GPA": 6.5,
    "CGPA": 6.7,

    "Gender": "Male",
    "Internet_Access": "Yes",
    "Part_Time_Job": "No",
    "Scholarship": "No",
    "Semester": 4,
    "Department": "Computer Science",
    "Parental_Education": "Graduate"
}


result = predict_dropout(student)

print(result)