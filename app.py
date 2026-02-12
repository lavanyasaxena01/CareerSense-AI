import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "career_model.pkl")

model = joblib.load(model_path)

import streamlit as st
import pandas as pd

st.set_page_config(page_title="CareerSense AI", layout="wide")

st.title("🎓 CareerSense AI")
st.write("AI Powered Career Guidance System")

interest = st.selectbox("Select Your Interest", ["Tech","Business","Creative"])
education = st.selectbox("Education Level", ["BTech","Any"])

if st.button("Recommend Career"):
    model = joblib.load("models/career_model.pkl")

    input_df = pd.DataFrame([[interest, education]], columns=["interest","education"])
    
    st.success("Recommended Career: Data Scientist")


