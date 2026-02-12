import streamlit as st
import os
import joblib
import pandas as pd

st.set_page_config(page_title="CareerSense AI", layout="wide")

st.title("🎓 CareerSense AI")
st.write("AI-Powered Career Guidance System")

# Load model safely
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, "career_model.pkl")
    model = joblib.load(model_path)
    st.success("Model Loaded Successfully ✅")
except Exception as e:
    st.error("Error loading model")
    st.write(e)

# --- USER INPUT SECTION ---
st.subheader("Enter Your Details")

interest = st.selectbox("Select Interest", ["Tech", "Business", "Creative"])
education = st.selectbox("Education Level", ["BTech", "Any"])

if st.button("Recommend Career"):
    st.write("Processing...")

    # Dummy result for now
    st.success("🎯 Recommended Career: Data Scientist")
    st.info("Salary Range: 8–15 LPA")
    st.warning("Demand: High")

    st.markdown("### 📌 Why This Career?")
    st.write("Based on your interest in Tech and educational background, Data Science aligns well with your analytical profile.")

    st.markdown("### 🚀 6-Month Roadmap")
    st.write("""
    - Month 1–2: Python + SQL  
    - Month 3–4: Machine Learning  
    - Month 5: Projects  
    - Month 6: Internship preparation  
    """)
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":
         f"Explain why {career} is suitable and give a 6 month roadmap."}
    ]
)

st.write(response.choices[0].message.content)
