import pickle
import numpy
import streamlit as st

# LOAD SAVE MODEL
model = pickle.load(open('kidney.sav', 'rb'))

# JUDUL WEB
st.title('PREDICTION CHRONIC KIDNEY DISEASE')

col1, col2, col3 = st.columns(3)

with col1:
    Bp = st.number_input('Blood Preasure')

with col2:
    Sg = st.number_input('Specific Gravity')

with col3:
    Al = st.number_input('Albumin')

with col1:
    Su = st.number_input('Sugar')

with col2:
    Rbc = st.number_input('Red Blood Cell')

with col3:
    Bu = st.number_input('Blood Urea')

with col1:
    Sc = st.number_input('Serum Creatinine')

with col2:
    Sod = st.number_input('Sodium')

with col3:
    Pot = st.number_input('Pottasium')

with col1:
    Hemo = st.number_input('Hemoglobin')

with col2:
    Wbcc = st.number_input('White Blood Cell Count')

with col3:
    Rbcc = st.number_input('Red Blood Cell Count')

with col1:
    Htn = st.number_input('Hypertension')


# CODE FOR PREDICTION
kidney_diagnosis = ''

# MEMBUAT TOMBOL PREDIKSI
if st.button('CHEK'):
    kidney_prediction = model.predict([[Bp, Sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])

    if (kidney_prediction[0]==1):
        kidney_diagnosis = 'Pasien Mengidap Ginjal Kronis'
    else:
        kidney_diagnosis = 'Pasien Tidak Mengidap Ginjal Kronis'
st.success(kidney_diagnosis)
