import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.set_page_config(page_title="Insurance Charges Predictor", page_icon="💰", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .big-font { font-size:24px !important; font-weight: bold; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; }
        .stTextInput>div>div>input { font-size: 18px; }
        .stNumberInput>div>div>input { font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-font'>Medical Insurance Charges Predictor 💰</h1>", unsafe_allow_html=True)
st.write("Fill in the details below to estimate your insurance charges.")

# Layout for inputs
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("**Age**", min_value=18, max_value=100, value=30)
    bmi = st.number_input("**BMI**", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
with col2:
    children = st.number_input("**Number of Children**", min_value=0, max_value=10, value=0, step=1)
    smoker = st.radio("**Smoker**", ("No", "Yes"), horizontal=True)

# Convert categorical input
smoker = 1 if smoker == "Yes" else 0

# Prepare input data
input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker]
})

# Predict button
if st.button("💡 Predict Charges"):
    prediction = model.predict(input_data)[0]
    st.markdown(f"""
        <div style='padding: 20px; background-color: #f4f4f4; border-radius: 10px;'>
            <h3>Predicted Insurance Charges:</h3>
            <h2 style='color: #4CAF50;'>${prediction:.2f}</h2>
        </div>
    """, unsafe_allow_html=True)
