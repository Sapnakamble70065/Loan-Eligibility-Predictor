import streamlit as st
import numpy as np
import joblib

# Load Model & Scaler
model = joblib.load('loan_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Loan Eligibility Predictor", page_icon="💸", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💸 Loan Eligibility Predictor 💸</h1>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Fill in your details below 👇")

# ----------------- User Inputs ------------------
language = st.selectbox("Select Language / Seleccionar idioma", ["English", "Español (Spanish)"])

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income (₹)", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income (₹)", min_value=0)
loan_amount = st.number_input("Loan Amount (₹)", min_value=0)
loan_amount_term = st.selectbox("Loan Term (Months)", [360, 180, 120, 84])
credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# -------------- Data Encoding -------------------
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents_map = {"0": 0, "1": 1, "2": 2, "3+": 3}
dependents = dependents_map[dependents]
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
property_area_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}
property_area = property_area_map[property_area]

input_data = np.array([
    gender, married, dependents, education, self_employed,
    applicant_income, coapplicant_income, loan_amount,
    loan_amount_term, credit_history, property_area
]).reshape(1, -1)

input_data = scaler.transform(input_data)

# -------------------- Prediction ---------------------
if st.button("Predict Eligibility 💡"):
    prediction = model.predict(input_data)
    if language == "Español (Spanish)":
        result = "✅ Aprobado para el préstamo" if prediction[0] == 1 else "❌ Rechazado para el préstamo"
    else:
        result = "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Rejected"

    st.markdown("---")
    st.success(result)
