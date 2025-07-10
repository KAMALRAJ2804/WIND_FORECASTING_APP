import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('xgb_wind_model.pkl')

# Title
st.title("ð¬ï¸ Wind Speed Forecasting using XGBoost")

# Input fields
pressure = st.number_input("Pressure (mbar)", min_value=900.0, max_value=1100.0, value=1010.0)
temperature = st.number_input("Temperature (Â°C)", min_value=0.0, max_value=50.0, value=25.0)
wind_20m = st.number_input("20m Wind Speed (m/s)", min_value=0.0, max_value=25.0, value=5.0)

# Predict button
if st.button("Predict 100m_N_Avg Wind Speed"):
    input_data = np.array([[pressure, temperature, wind_20m]])
    prediction = model.predict(input_data)[0]
    st.success(f"ð¨ Predicted Wind Speed at 100m_N: {round(prediction, 2)} m/s")
