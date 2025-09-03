# app.py

import streamlit as st
import numpy as np
import joblib

st.title("⚡ Energy Consumption Predictor & Optimizer")

model = joblib.load(r"C:\Users\bhupe\Downloads\predict_energy_consumption(in).csv")

temp = st.slider("Temperature (°C)", 10, 45, 25)
humidity = st.slider("Humidity (%)", 10, 100, 50)
hours = st.slider("Appliance Usage Hours per Day", 1, 24, 6)

if st.button("Predict Energy Usage"):
    data = np.array([[temp, humidity, hours]])
    prediction = model.predict(data)[0]
    
    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")

    st.subheader("⚙️ Optimization Suggestion")
    suggestions = []
    if hours > 6:
        suggestions.append("- Reduce usage hours below 6 for savings.")
    if temp > 30:
        suggestions.append("- Consider better insulation or cooling.")
    if humidity > 60:
        suggestions.append("- Use dehumidifiers to save energy.")
    if not suggestions:
        st.info("✅ Your usage is already efficient!")
    else:
        for tip in suggestions:
            st.write(tip)
