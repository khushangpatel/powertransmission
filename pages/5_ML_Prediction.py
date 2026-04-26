import streamlit as st
import pandas as pd
from ml_model import train_model
from data_loader import load_data
from prediction_db import save_prediction

st.title("ML Budget Overrun Prediction")

df = load_data()

model, features, acc, prec = train_model(df)

st.subheader("Model Performance")
st.write(f"Accuracy: {round(acc * 100, 2)}%")
st.write(f"Precision: {round(prec * 100, 2)}%")

st.subheader("Enter Project Details")

length = st.number_input("Transmission Line Length (km)", min_value=1, value=50)
voltage = st.selectbox("Voltage Level (kV)", [132, 220, 400, 765])
duration = st.number_input("Planned Duration (Months)", min_value=1, value=12)

experience = st.slider("Contractor Experience (years)", 1, 20, 10)
material_index = st.slider("Material Cost Index", 1.0, 1.5, 1.2)
labor = st.slider("Labor Availability (%)", 50, 100, 80)

if st.button("Predict Overrun Probability"):

    input_data = pd.DataFrame(
        [[length, voltage, duration, experience, material_index, labor]],
        columns=features
    )

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error("High Probability of Budget Overrun")
    else:
        st.success("Low Probability of Budget Overrun")

    st.write(f"Overrun Probability: {round(probability * 100, 2)}%")

    save_prediction(length, voltage, duration, int(prediction), float(probability))