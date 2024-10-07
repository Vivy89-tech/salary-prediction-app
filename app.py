
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Load your model file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


st.title('Salary Prediction App')

# first column
# Add input widgets for user inputs
work_location_borough = st.selectbox(
  "Work_location_borough",
  ["MANHATTAN", "QUEENS", "BROOKLYN", "BRONX"]
)

title_description = st.selectbox(
  "Title_description",
  [
    'PRINCIPAL ADMINISTRATIVE ASSOCIATE -  NON SUPVR',
    'YOUTH DEVELOPMENT SPECIALIST',
    'CHILD PROTECTIVE SPECIALIST SUPERVISOR',
    'COMMUNITY COORDINATOR',
    'INSTITUTIONAL AIDE',
    'PROGRAM EVALUATOR',
    'CHILD PROTECTIVE SPECIALIST',
    'SPECIAL OFFICER',
    'ADMINISTRATIVE DIRECTOR OF SOCIAL SERVICES',
    'PROTECTION AGENT',
    'ASSOCIATE STAFF ANALYST',
    'ADM MANAGER-NON-MGRL',
    'COMMUNITY ASSOCIATE',
    'ADMINISTRATIVE STAFF ANALYST',
    'CLERICAL ASSOCIATE',
    'ASSISTANT COMMISSIONER FOR FACILITIES OPERATIONS',
    'DIRECTOR OF FIELD OPERATIONS',
    'CASEWORKER',
    'SUPERVISING SPECIAL OFFICER'
    'ADMINISTRATIVE DIRECTOR OF RESIDENTIAL CHILD CARE',
    'SUPERVISOR II'
    'STAFF NURSE' 'AGENCY ATTORNEY',
    'SUPERVISOR OF NURSES'
    'CHILD WELFARE SPECIALIST',
    'COMPUTER ASSOCIATE'
    'EXECUTIVE AGENCY COUNSEL',
    'COMPUTER SPECIALIST' 'MOTOR VEHICLE OPERATOR'
    'CHILD WELFARE SPECIALIST SUPERVISOR',
    'CITY RESEARCH SCIENTIST',
    'CONGREG CARE SPEC - ACS',
    'PARALEGAL AIDE',
    'AGENCY ATTORNEY INTERNE',
    'SUPERVISOR III',
    'SUPERVISOR I',
    'STAFF ANALYST' 'CONGREG CARE SPEC- DJJ'
    'ASSOCIATE YOUTH DEVELOPMENT SPECIALIST' 'CHILD AND FAMILY SPECIALIST'
    '*COOK' 'COMPUTER SERVICE TECHNICIAN' 'PLUMBER' 'INVESTIGATOR'
    'ASST COMMISSIONER FOR NON-SECURE DETENTION JUVENILE JUSTICE'
    'COMPUTER SYSTEMS MANAGER' 'ASSISTANT COMMISSIONER'
    'ASSOCIATE INVESTIGATOR' 'SUMMER COLLEGE INTERN'
    'TELECOMMUNICATIONS ASSOCIATE' 'ADMIN COMMUNITY RELATIONS SPECIALIST'
    'RESEARCH ASSISTANT' 'COMMUNITY ASSISTANT'
    'EXEC ASST TO THE DEPUTY COMMISSIONER' 'DEPUTY GENERAL COUNSEL'
    'DIRECTOR OF PUBLIC INFORMATION' 'CITY LABORER'
    'ADMIN CONSTRUCTION PROJECT MANAGER' 'CARPENTER' '*ATTORNEY AT LAW'
    'ADMINISTRATIVE NUTRITIONIST' 'ARCHITECT' 'MANAGEMENT AUDITOR'
    'SUPERVISING COMPUTER SERVICE TECHNICIAN' 'CONFIDENTIAL STRATEGY PLANNER'
    'PROCUREMENT ANALYST' '*SENIOR COOK'
  ]

)

pay_basis = st.selectbox(
  "Pay_basis",
  ['per Annum',
   'per Day',
   'per Hour']
)
regular_hours = st.slider("Regular_hours:",
 0, 3000, 1800)


# click 'Predict' Button to make a prediction

if st.button("Predict"):

  # Prepare the input data as a DataFrame (since pipelines often expect a DataFrame)
  input_data = pd.DataFrame({
    'Work_location_borough': [work_location_borough],
    'Title_description': [title_description],
    'Pay_basis': [pay_basis],
    'Regular_hours': [regular_hours]

  }, index=[0])
  prediction = model.predict(input_data)[0].round(2)
  st.write(f'The predicted value is: {prediction} thousand dollars')
