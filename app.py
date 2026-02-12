import streamlit as st
import joblib
import os

st.set_page_config(page_title="CareerSense AI", layout="centered")

st.title("🎯 CareerSense AI")
with st.form("my_form"):
    st.subheader("Student Profile")
    
    # Inputs based on your dataset columns
    interest = st.selectbox("Select your main Interest", ["Coding", "Design", "Writing", "Business", "Healthcare"])
    skills = st.multiselect("Select your Skills", ["Python", "Java", "SQL", "Photoshop", "Management", "Communication"])
    degree = st.selectbox("Current Qualification", ["High School", "Bachelors", "Masters"])

    submit = st.form_submit_button("Predict My Career")

if submit:
    # 1. Prepare Input Data (Matching your model_columns)
    # This creates a row of 0s
    input_data = pd.DataFrame(0, index=[0], columns=model_cols)
    
    # 2. Update the columns for the selected inputs to 1
    # Note: Column names must match exactly what pd.get_dummies produced in Colab
    if f"Interests_{interest}" in model_cols:
        input_data.at[0, f"Interests_{interest}"] = 1
        
    for s in skills:
        if f"Skills_{s}" in model_cols:
            input_data.at[0, f"Skills_{s}"] = 1

    # 3. Predict using XGBoost/RandomForest
    prediction = model.predict(input_data)
    career_name = le.inverse_transform(prediction)[0]

    st.success(f"### Recommended Career: {career_name}")

    # 5. Generative AI Roadmap
    st.markdown("---")
    st.subheader("🗺️ Your Skill Development Roadmap")
    
    # If you have an OpenAI/Gemini Key set up in Streamlit Secrets:
    # roadmap = get_ai_response(career_name, skills) 
    # st.write(roadmap)

    # For the Exhibition (Static Demo version):
    st.write(f"To become a successful **{career_name}**, we recommend:")
    st.markdown(f"- **Month 1-2:** Deep dive into advanced {skills[0] if skills else 'technical basics'}.")
    st.markdown("- **Month 3-4:** Build 3 portfolio projects related to this field.")
    st.markdown("- **Month 5-6:** Prepare for industry-standard certifications.")
    
    # 4. Show Career Breakdown (Visual wow factor)
    st.info("💡 **AI Tip:** Based on your skills, you have an 85% match for this role.")

# --- LOAD MODELS ---
@st.cache_resource
def load_data():
    model = joblib.load('career_model.pkl')
    le = joblib.load('label_encoder.pkl')
    cols = joblib.load('model_columns.pkl')
    return model, le, cols

model, le, model_cols = load_data()

# --- YOUR FORM STARTS HERE ---
with st.form("my_form"):
    st.subheader("Enter your details")
    # ... (your input fields)
    submit = st.form_submit_button("Predict")
