import streamlit as st
import pandas as pd
import joblib
import os

# 1. Page Configuration
st.set_page_config(page_title="CareerSense AI", layout="centered", page_icon="🎯")

# 2. Model Loading Logic (Must happen before the form uses the variables)
@st.cache_resource
def load_data():
    # Ensure these filenames match exactly what you uploaded to GitHub
    model = joblib.load('career_model.pkl')
    le = joblib.load('label_encoder.pkl')
    cols = joblib.load('model_columns.pkl')
    return model, le, cols

try:
    model, le, model_cols = load_data()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# 3. Main UI
st.title("🎯 CareerSense AI")
st.write("Intelligent career guidance powered by Machine Learning.")

# 4. The Unified Input Form (ONE form only)
with st.form("career_analysis_form"):
    st.subheader("Student Profile")
    
    col1, col2 = st.columns(2)
    with col1:
        # Use the interests your model was actually trained on
        interest = st.selectbox("Primary Interest", ["Coding", "Design", "Writing", "Business", "Healthcare"])
        degree = st.selectbox("Qualification", ["High School", "Bachelors", "Masters"])
    
    with col2:
        skills = st.multiselect("Your Skills", ["Python", "Java", "SQL", "Photoshop", "Management", "Communication"])
    
    submit = st.form_submit_button("Predict My Career Path")

# 5. Prediction Logic
if submit:
    # Prepare Input Data (Matching your model_columns)
    input_data = pd.DataFrame(0, index=[0], columns=model_cols)
    
    # Fill in user selections (Mapping text to binary columns)
    if f"Interests_{interest}" in model_cols:
        input_data.at[0, f"Interests_{interest}"] = 1
        
    for s in skills:
        if f"Skills_{s}" in model_cols:
            input_data.at[0, f"Skills_{s}"] = 1

    # Predict
    prediction = model.predict(input_data)
    career_name = le.inverse_transform(prediction)[0]

    # Display Results
    st.success(f"### Recommended Career: {career_name}")
    st.info("💡 **AI Match Score:** Based on your profile, you are a strong match for this field.")

    # 6. Roadmap Section
    st.divider()
    st.subheader("🗺️ Your Skill Development Roadmap")
    st.write(f"To succeed as a **{career_name}**, follow this path:")
    
    # Logic to handle empty skill selection for the roadmap display
    focus_skill = skills[0] if skills else "fundamental technical skills"
    
    st.markdown(f"""
    - **Months 1-2:** Deep dive into advanced {focus_skill} and industry standards.
    - **Months 3-4:** Build 3 portfolio projects specifically for {career_name} roles.
    - **Months 5-6:** Prepare for professional certifications and begin networking.
    """)
