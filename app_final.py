import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.joblib')
LE = joblib.load('LE.joblib')
ss = joblib.load('Scaling.joblib')



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
    
    cat_col = [gender, Marital_Status, Work_Type, Residence_type, smoking_status]
    encoded_cat = LE.transform([cat_col])

    num_col = [Age, Hypertension_status, Heart_Disease, Glucose_level, BMI_value]
    scaled_num = ss.transform([num_col])

    final_features = np.concatenate((scaled_num, encoded_cat), axis=1)

    prediction = model.predict(final_features)
    result = prediction[0]

    # Result
    if result == 1:
        st.error("Student may have Depression")
    else:
        st.success("Student may not have Depression")