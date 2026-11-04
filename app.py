import streamlit as st
import pandas as pd
import joblib

model = joblib.load("employee_attrition_model.pkl")
scaler = joblib.load("employee_attrition_scaler.pkl")
st.title("Employee Attrition Prediction")

Age=st.number_input("Age", min_value=18, max_value=65, value=30)
Gender=st.selectbox("Gender", ["Male", "Female"])
Department=st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
BusinessTravel=st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
DistanceFromHome=st.number_input("Distance From Home (in miles)", min_value=1, max_value=100, value=10)
MonthlyIncome=st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000)
OverTime=st.selectbox("OverTime", ["Yes", "No"])
JobSatisfaction=st.slider("Job Satisfaction", min_value=1, max_value=4, value=3)
EnvironmentSatisfaction=st.slider("Environment Satisfaction", min_value=1, max_value=4, value=3)
WorkLifeBalance=st.slider("Work-Life Balance", min_value=1, max_value=4, value=3)
YearsAtCompany=st.number_input("Years at Company", min_value=0, max_value=40, value=5)
TotalWorkingYears=st.number_input("Total Working Years", min_value=0, max_value=40, value=10)
if st.button("Predict Attrition"):
    input_data = pd.DataFrame({
    "Age":[Age],
    "Gender":[1 if Gender=="Male" else 0],
    "Department":[Department],
    "BusinessTravel":[BusinessTravel],
    "DistanceFromHome":[DistanceFromHome],
    "MonthlyIncome":[MonthlyIncome],
    "OverTime":[1 if OverTime=="Yes" else 0],
    "JobSatisfaction":[JobSatisfaction],
    "EnvironmentSatisfaction":[EnvironmentSatisfaction],
    "WorkLifeBalance":[WorkLifeBalance],
    "YearsAtCompany":[YearsAtCompany],
    "TotalWorkingYears":[TotalWorkingYears]})
    
    input_data = pd.get_dummies(
    input_data,
    columns=["Department","BusinessTravel"])
    training_columns = joblib.load("training_columns.pkl")

    input_data = input_data.reindex(
        columns=training_columns,
        fill_value=0)

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.error("The employee is likely to leave the company.")    
    else:
        st.success("The employee is likely to stay with the company.")