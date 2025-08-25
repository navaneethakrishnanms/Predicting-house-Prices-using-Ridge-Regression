# app.py
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r"notebook\ridge_model.pkl", "rb"))


st.title("House Price Prediction using Ridge Regression")

size = st.number_input("Enter size (m²)", min_value=10.0)
bedrooms = st.number_input("Enter number of bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Enter number of bathrooms", min_value=1, step=1)
distance_city = st.number_input("Enter distance to city center (km)", min_value=0.0)
age_years = st.number_input("Enter age of house (years)", min_value=0.0)

if st.button("Predict"):
    features = np.array([[size, bedrooms, bathrooms, distance_city, age_years]])
    prediction = model.predict(features)
    st.success(f"Predicted Price: {prediction[0]:,.2f} ₹")
