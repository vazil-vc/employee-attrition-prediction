# Employee Attrition Prediction

A Machine Learning web application built using **Python, Scikit-learn, and Streamlit** to predict whether an employee is likely to leave the company based on employee-related information.

---

## Project Overview

Employee attrition is one of the biggest challenges for organizations. This project uses Logistic Regression to predict employee attrition based on historical employee data.

The application allows users to enter employee details through a simple Streamlit interface and instantly predicts whether the employee is likely to stay or leave.

---

## Features

- Data Cleaning
- Missing Value Handling
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Logistic Regression Model
- Streamlit Web Application
- Model Serialization using Joblib

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Missing Value Imputation
4. Feature Encoding
5. Feature Scaling
6. Train-Test Split
7. Logistic Regression Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment

---

## Project Structure

```
Employee-Attrition-Prediction/
│
├── app.py
├── employee_attrition_prediction.ipynb
├── employee_attrition_model.pkl
├── employee_attrition_scaler.pkl
├── training_columns.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 85% |
| Precision | 61% |
| Recall | 40% |
| F1 Score | 48% |

---

## Running the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Employee-Attrition-Prediction.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
streamlit run app.py
```

---

## Application Screenshot

Add a screenshot here after running the application.

```
images/app_screenshot.png
```

---

## Future Improvements

- Random Forest Classifier
- XGBoost
- Hyperparameter Tuning
- Feature Selection (RFE)
- Model Deployment on Streamlit Cloud

---

## Author

Your Name

GitHub:
https://github.com/yourusername