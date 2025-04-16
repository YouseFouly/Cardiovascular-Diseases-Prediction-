# -*- coding: utf-8 -*-
"""
Created on Thu Sep 5 13:52:40 2024

@author: ELBOSTAN
"""

import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu 

diabetes_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/Turkey/diabetes_model.sav', 'rb'))
heart_failure_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/Turkey/heart failure model.sav', 'rb'))
obesity_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/Turkey/obesity_model.sav', 'rb'))
storkes_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/Turkey/strokes_model.sav', 'rb'))

    
    
with st.sidebar:
    selected = option_menu('Cardiovascular Diseases (CVDs) ❤️ ',
                           ['Diabetes Prediction',
                            'Heart Failure Prediction',
                            'Obesity Prediction',
                            'Strokes Prediction'],
                            icons = ['activity','heart','heart-pulse','postcard-heart-fill'],        
                            default_index = 0)

#diabetes prediction page 
if selected == 'Diabetes Prediction':
    
    #page title
    st.title('Diabetes Prediction🧬')
    
    #Getting the input data from user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
        #code for prediction 
        diab_diagnosis = ''
        
        #creating a button for prediction
        if st.button('Diabetes Prediction Results'):
            
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age] 
            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)

            
            
if selected == 'Heart Failure Prediction':
    
    # Page title
    st.title('Heart Failure Prediction🫀')
    
    # Getting the input data from user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
       Sex = st.selectbox('Gender', ['','Female', 'Male'])
       Sex = 0 if Sex == 'Female' else 1
       
    with col3:
        ChestPainType = st.selectbox('ChestPainType', ['', 'ATA','NAP','ASY', 'TA'])

        if ChestPainType == 'ATA':
            ChestPainType = 0
        elif ChestPainType == 'NAP':
            ChestPainType = 1
        elif ChestPainType == 'ASY':
            ChestPainType = 2
        else:
            ChestPainType = 3
            
    with col1:
        RestingBP = st.text_input('Resting blood pressure [mm Hg]')
    
    with col2:
        Cholesterol = st.text_input('Cholesterol [mg/dl]')
    
    with col3:
        FastingBS = st.text_input('Fasting blood sugar [1: if >120 mg/dl, 0: otherwise]')
    
    with col1:
        RestingECG = st.selectbox('Resting ECG', ['','Normal', 'ST', 'LVH'])

        if RestingECG == 'Normal':
            RestingECG = 0
        elif RestingECG == 'ST':
            RestingECG = 1
        else:
            RestingECG = 2
    
    with col2:
        MaxHR = st.text_input('Maximum heart rate')
        
    with col3:
        ExerciseAngina = st.selectbox('Exercise-induced angina', ['','Yes', 'No'])
        ExerciseAngina = 0 if ExerciseAngina == 'No' else 1
     
    with col1:
        Oldpeak = st.text_input('Oldpeak [Numeric value - depression]')
     
    with col2:
        ST_Slope = st.selectbox('ST Slope', ['', 'Up', 'Flat','Down'])
        if ST_Slope == 'Up':
            ST_Slope = 0
        elif ST_Slope =='Flat':
            ST_Slope = 1
        else:
            ST_Slope = 2
            
        

    # Code for prediction
    diss_diagnosis = ''
    
    if st.button('Heart Failure Prediction Results'):
        try:
            user_input = [
                Age, Sex, ChestPainType, RestingBP, Cholesterol,
                FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope
            ]
            user_input = [float(x) for x in user_input]
    
            diss_prediction = heart_failure_model.predict([user_input])
           
            if diss_prediction[0] == 1:
                diss_diagnosis = 'The person has a heart disease'
            else:
                diss_diagnosis = 'The person does not have a heart disease'
        except Exception as e:
            diss_diagnosis = f'Error: {e}'
    
    st.success(diss_diagnosis)

     

if selected == 'Obesity Prediction':
    
    #page title
    st.title('Obesity Prediction🍔')
    
    
    #Getting the input data from user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')

    with col2:
        Gender = st.selectbox('Gender', ['','Female', 'Male'])
        Gender = 0 if Gender == 'Female' else 1
    
    with col3:
        Height = st.text_input('Height')
    
    with col1:
        Weight = st.text_input('Weight')
    
    with col2:
        BMI = st.text_input('BMI')
    
    with col3:
        PhysicalActivityLevel = st.text_input('Physical Activity Level')

    #code for prediction 
    obesity_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Obesity Prediction Results'):
        
        user_input = [Age, Gender, Height, Weight, BMI, PhysicalActivityLevel] 
        user_input = [float(x) for x in user_input]
  
        obesity_prediction = obesity_model.predict([user_input])
        
            
        if obesity_prediction[0] == 0:
           obesity_diagnosis = 'The person is Normal'
        
        elif obesity_prediction[0] == 1:
             obesity_diagnosis = 'The person is Overweight'
        
        elif obesity_prediction[0] == 2:
             obesity_diagnosis = 'The person is Obese'
        else :
            obesity_diagnosis = 'The person is Underweight'
  
    st.success(obesity_diagnosis)       
     
 
if selected == 'Strokes Prediction':
    
    #page title
    st.title('Strokes Prediction🧠')
    
    #Getting the input data from user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox('Gender', ['','Female', 'Male'])
        gender = 0 if gender == 'Female' else 1
    with col2:
        age = st.text_input('Age')
    
    with col3:
        hypertension = st.selectbox('Hypertension', ['', 'No', 'Yes'])
        if hypertension == 'No':
            hypertension = 0
        elif hypertension == 'Yes':
            hypertension = 1
        else:
            hypertension = None
    
    with col1:
        heart_disease = st.selectbox('Heart Disease', ['', 'No', 'Yes'])
        if heart_disease == 'No':
            heart_disease = 0
        elif heart_disease == 'Yes':
            heart_disease = 1
        else:
            heart_disease = None
    
    with col2:
        ever_married = st.selectbox('Ever Married?', ['', 'No', 'Yes'])
        if ever_married == 'No':
            ever_married = 0
        elif ever_married == 'Yes':
            ever_married = 1
        else:
            ever_married = None
    
    with col3:
        Residence_type = st.selectbox('Residence Type', ['', 'Rural', 'Urban'])
        if Residence_type == 'Rural':
            Residence_type = 0
        elif Residence_type == 'Urban':
            Residence_type = 1
        else:
            Residence_type = None
    
    with col2:
        avg_glucose_level = st.text_input('Average Glucose Level')  
        
    with col3:
        bmi = st.text_input('BMI')  
    
    with col1:
        smoking_status = st.selectbox(
            'Smoking Status',
            ['', 'Unknown', 'Never smoked', 'Formerly smoked', 'Smokes']
        )
        if smoking_status == 'Unknown':
            smoking_status = 0
        elif smoking_status == 'Smokes':
            smoking_status = 1
        elif smoking_status == 'Formerly smoked':
            smoking_status = 2
        elif smoking_status == 'Never smoked':
            smoking_status = 3
        else:
            smoking_status = None

    

    #code for prediction 
    strokes_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Strokes Prediction Results'):
        
        user_input = [gender, age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, smoking_status] 
        user_input = [float(x) for x in user_input]
  
        strokes_prediction = storkes_model.predict([user_input])
        
            
        if strokes_prediction[0] == 0:
           strokes_diagnosis = 'The person is not likely to get a stroke'
        
        else :
            strokes_diagnosis = 'The person is likely to get a stroke'
  
    st.success(strokes_diagnosis)       
    