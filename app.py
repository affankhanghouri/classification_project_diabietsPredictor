import pickle
import numpy as np
import streamlit as st

# Load the trained model
with open('diabitiesPipe.pkl', 'rb') as f:
    model = pickle.load(f)


# Streamlit UI
st.title("🩺 Diabetes Prediction App")

st.markdown("Enter the following health details to predict the likelihood of having diabetes.")

# Input fields
pregnancies = st.number_input("Number of Pregnancies:", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose Level (mg/dL):", min_value=0, max_value=300, step=1)
blood_pressure = st.number_input("Blood Pressure (mm Hg):", min_value=0, max_value=200, step=1)
skin_thickness = st.number_input("Skin Thickness (mm):", min_value=0, max_value=100, step=1)
insulin = st.number_input("Insulin Level (IU/mL):", min_value=0, max_value=900, step=1)
bmi = st.number_input("BMI:", min_value=0.0, max_value=60.0, step=0.1)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function:", min_value=0.0, max_value=2.5, step=0.01)
age = st.number_input("Age:", min_value=0, max_value=120, step=1)

# Predict diabetes
if st.button("Predict Diabetes 🏥"):
    input_features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        st.error("🚨 High Risk: The person **likely** has diabetes.")
    else:
        st.success("✅ Low Risk: The person **likely does not** have diabetes.")
