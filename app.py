import streamlit as st
import os
import joblib

st.title("🎓 CareerSense AI")

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, "career_model.pkl")
    
    model = joblib.load(model_path)
    st.success("Model Loaded Successfully ✅")

except Exception as e:
    st.error("Error loading model")
    st.write(e)
