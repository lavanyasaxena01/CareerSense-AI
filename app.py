import streamlit as st
import joblib
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


