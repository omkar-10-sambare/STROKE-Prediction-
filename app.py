import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.joblib')
encoders = joblib.load('encoders.joblib')
ss = joblib.load('Scaling.joblib')

st.title("STROKE ANALYSIS")

gender = st.selectbox("gender", ["Male","Female"])
Marital_Status = st.selectbox("ever_married", ["Yes","No"])
Work_Type = st.selectbox("work_type", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
Residence_type = st.selectbox("Residence_type", ['Urban', 'Rural'])
smoking_status = st.selectbox("smoking_status", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

Age = st.number_input("age",min_value=1,max_value=100,value=25)
Hypertension_status = st.slider("hypertension",min_value=0,max_value=1,value=0)
Heart_Disease = st.slider("heart_disease",min_value=0,max_value=1,value=0)
Glucose_level = st.number_input("avg_glucose_level",min_value=56,max_value=270,value=70)
BMI_value = st.number_input("bmi",min_value=0,max_value=100,value=18)


if st.button("Click to know the result"):
    
    gender_encoded = encoders['gender'].transform([gender])[0]
    marital_encoded = encoders['ever_married'].transform(
        [Marital_Status]
    )[0]

    work_encoded = encoders['work_type'].transform(
        [Work_Type]
    )[0]

    residence_encoded = encoders['Residence_type'].transform(
        [Residence_type]
    )[0]

    smoking_encoded = encoders['smoking_status'].transform(
        [smoking_status]
    )[0]

    
    
    num_col = [[
        Age,
        Hypertension_status,
        Heart_Disease,
        Glucose_level,
        BMI_value
    ]]

    scaled_num = ss.transform(num_col)

    categorical_features = np.array([[
        gender_encoded,
        marital_encoded,
        work_encoded,
        residence_encoded,
        smoking_encoded
    ]])

    final_features = np.concatenate(
        (scaled_num, categorical_features),
        axis=1
    )
    
    prediction = model.predict(final_features)
    result = prediction[0]

    # Result
    if result == 1:
        st.error("The person may have a stroke.")
    else:
        st.success("The person may not have a stroke.")