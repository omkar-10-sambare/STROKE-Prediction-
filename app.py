import streamlit as st
import pandas as pd


Gender = st.selectbox("gender", ["Male","Female"])
input_df = pd.DataFrame([[Gender]],columns =["Gender1"])
Encoded_Gender = LE.transform(input_df)
gender_value = Encoded_Gender[0][0]

Marital_Status = st.selectbox("ever_married", ["Yes","No"])
input_df = pd.DataFrame([[Marital_Status]],columns =["Marital_Status"])
Encoded_Marital_Status = LE.transform(input_df)
Married_Status_value = Encoded_Marital_Status[0][0]

Work_Type = st.selectbox("work_type", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
input_df = pd.DataFrame([[Work_Type]],columns =["Work_Type"])
Encoded_Work_Type = LE.transform(input_df)
Work_Type_value = Encoded_Work_Type[0][0]

Residence_type = st.selectbox("Residence_type", ['Urban', 'Rural'])
input_df = pd.DataFrame([[Residence_type]],columns =["Residence_type"])
Encoded_Residence_type = LE.transform(input_df)
Encoded_Residence_type_value = Encoded_Residence_type[0][0]


smoking_status = st.selectbox("smoking_status", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])
input_df = pd.DataFrame([[smoking_status]],columns =["smoking_status"])
Encoded_smoking_status = LE.transform(input_df)
smoking_status_value = Encoded_smoking_status[0][0]

Age = st.number_input("age",min_value=1,max_value=100,value=25)
input_array = np.array(Age).reshape(1,-1)
scaled_age = ss.transform(input_array)
scaled_age_value = scaled_age[0][0]

Hypertension_status = st.slider("hypertension",min_value=0,max_value=1,value=0)
input_array = np.array(Hypertension_status).reshape(1,-1)
scaled_hypertension = ss.transform(input_array)
scaled_hypertension_value = scaled_hypertension[0][0]

Heart_Disease = st.slider("heart_disease",min_value=0,max_value=1,value=0)
input_array = np.array(Heart_Disease).reshape(1,-1)
scaled_heart_disease = ss.transform(input_array)
scaled_heart_disease_value = scaled_heart_disease[0][0]

Glucose_level = st.number_input("avg_glucose_level",min_value=56,max_value=270,value=70)
input_array = np.array(Glucose_level).reshape(1,-1)
scaled_glucose_level = ss.transform(input_array)
scaled_glucose_level_value = scaled_glucose_level[0][0]

BMI_value = st.number_input("bmi",min_value=0,max_value=100,value=18)
input_array = np.array(BMI_value).reshape(1,-1)
scaled_bmi = ss.transform(input_array)
scaled_bmi_value = scaled_bmi[0][0]



input = [gender_value,Married_Status_value,Work_Type_value,Encoded_Residence_type_value,smoking_status_value,scaled_age_value,
         scaled_hypertension_value,scaled_heart_disease_value,scaled_glucose_level_value,scaled_bmi_value]

if st.button("Predict"):
    input_2d = np. array(input).reshape(1,10)
    prediction[0] = model.predict(input_2d)
    result = prediction[0]

    if result ==0:
        st.success("Congratulations! You are at low risk of having STROKE :)")
    else:
        st.error("Take Care of your health! You are at HIGH risk of having STROKE :(")
