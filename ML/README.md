# Student Dropout Risk Prediction System - ML Backend

This folder contains the machine-learning and backend component of the **Student Dropout Risk Prediction System**.

The system takes student information, predicts the probability of dropout risk, identifies the student's risk level, explains the major factors contributing to that risk, and generates relevant recommendations.

## How It Works

The ML backend follows this flow:

```text
Student Data
     ↓
FastAPI /predict
     ↓
Input Validation
     ↓
Preprocessing
     ↓
Trained ML Model
     ↓
Dropout Probability
     ↓
Risk Level
     ↓
Risk Factor Explanation
     ↓
Recommendations
     ↓
JSON Response
```

The system produces:

* **Risk probability**
* **Risk percentage**
* **Risk level**
* **Risk-increasing factors**
* **Risk-reducing factors**
* **Recommendations based on the risk factors**

### Risk Levels

| Probability     | Risk Level |
| --------------- | ---------- |
| `< 0.40`        | Low        |
| `0.40 - < 0.60` | Medium     |
| `≥ 0.60`        | High       |

The final prediction threshold used by the system is **0.60**.

---

## Project Structure

```text
ML/
├── api/
│   └── main.py
│
├── models/
│   └── dropout_model.joblib
│
├── src/
│   ├── predict.py
│   ├── explain_model.py
│   ├── explain.py
│   ├── recommendations.py
│   └── student_risk.py
│
└── requirements.txt
```

### `src/predict.py`

Handles the actual prediction.

* Loads `dropout_model.joblib`
* Accepts raw student data
* Returns dropout probability
* Determines the risk level

### `src/explain_model.py`

Handles model explainability using the trained Logistic Regression model.

* Calculates feature contributions
* Identifies factors that increase risk
* Identifies factors that reduce risk
* Converts model feature names into human-readable labels

### `src/explain.py`

Contains higher-level explanation functionality used by the project.

### `src/recommendations.py`

Generates recommendations based on the student's:

* Risk level
* Contributing risk factors

Examples include:

* Academic mentoring
* Academic planning support
* Travel-related support
* Attendance intervention
* Wellbeing support

### `src/student_risk.py`

Combines the prediction, explanation, and recommendation components into one complete student risk assessment.

### `api/main.py`

Contains the FastAPI application.

It:

* Exposes `POST /predict`
* Validates student input using Pydantic
* Calls `student_risk.assess_student()`
* Returns the complete assessment as JSON

### `models/dropout_model.joblib`

Contains the saved trained model/pipeline used for prediction.

---

## Dataset

The model was developed using a dataset containing **10,000 student records**.

The dataset contains academic, demographic, financial, behavioral, and other student-related features.

Missing values were present in:

* `Family_Income`
* `Study_Hours_per_Day`
* `Stress_Index`
* `Parental_Education`

These missing values are handled by the preprocessing pipeline.

Categorical features are also encoded during preprocessing.

---

## Model Development

Three models were trained and compared:

* Logistic Regression
* Random Forest
* XGBoost

The project does not select a model based only on accuracy. Since the purpose is to identify students who may be at risk, **recall and ROC-AUC are important considerations**.

The final prediction system uses the trained model saved in:

```text
models/dropout_model.joblib
```

---

## API

The backend runs as a FastAPI application.

### Start the API

From the project root:

```bash
uvicorn ML.api.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger can be used to test the prediction API directly.

### Endpoint

```text
POST /predict
```

---

## Example Request

```json
{
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
  "Semester": "Year 4",
  "Department": "CS",
  "Parental_Education": "Master"
}
```

## Example Response

```json
{
  "risk_probability": 0.9351,
  "risk_percentage": 93.51,
  "risk_level": "High",
  "risk_factors": [
    {
      "factor": "GPA",
      "effect": "increases risk",
      "importance": "moderate"
    },
    {
      "factor": "Assignment delays",
      "effect": "increases risk",
      "importance": "moderate"
    }
  ],
  "risk_reducing_factors": [
    {
      "factor": "No part-time job",
      "effect": "reduces risk",
      "importance": "weak"
    }
  ],
  "recommendations": [
    {
      "type": "academic_support",
      "factor": "GPA",
      "title": "Academic mentoring",
      "description": "Provide targeted academic mentoring and subject-specific support.",
      "priority": "High"
    }
  ]
}
```

---

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

Make sure you are in the project root directory and run:

```bash
pip install -r ML/requirements.txt
```

The `requirements.txt` file contains the dependencies required by the ML backend, including:

* pandas
* scikit-learn
* joblib
* FastAPI
* Uvicorn
* Pydantic
* XGBoost, if required by the training notebook

---

## Running the Project

After installing the dependencies:

```bash
uvicorn ML.api.main:app --reload
```

Then open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Use:

```text
POST /predict
```

to send student data and receive the complete risk assessment.

---

## Architecture

```text
Frontend
   ↓
FastAPI /predict
   ↓
student_risk.py
   ├── predict.py
   ├── explain_model.py
   └── recommendations.py
   ↓
JSON Response
   ↓
Frontend
```

### In Short

```text
Input Student Data
        ↓
    Prediction
        ↓
  Risk Probability
        ↓
    Risk Level
        ↓
   Explanation
        ↓
 Recommendations
        ↓
   JSON Response
```

The ML backend therefore acts as the bridge between the student data and the frontend's student risk dashboard.
