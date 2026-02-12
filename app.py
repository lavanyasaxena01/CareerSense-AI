import joblib
import pandas as pd

model = joblib.load("models/career_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")
model_columns = joblib.load("models/model_columns.pkl")

import streamlit as st
import pandas as pd
import joblib
import random

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="CareerSense AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------
# Custom Styling
# -------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
}
.card {
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    background-color: #ffffff;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.markdown('<p class="main-title">🚀 CareerSense AI</p>', unsafe_allow_html=True)
st.write("An Intelligent Career Guidance & Skill Recommendation System")

st.divider()

# -------------------------------
# Load Model & Data
# -------------------------------
@st.cache_resource
def load_model():
    import joblib
    model = joblib.load("models/career_model.pkl")
    return model
    
model = load_model()


# -------------------------------
# Sidebar Input
# -------------------------------
st.sidebar.header("🎯 Enter Your Details")

skills = st.sidebar.multiselect(
    "Select Your Skills",
    ["Python", "Java", "C++", "Machine Learning", "Communication",
     "Design", "Marketing", "Data Analysis", "Leadership"]
)

interest = st.sidebar.selectbox(
    "Select Your Interest",
    ["Technology", "Business", "Creative", "Research"]
)

education = st.sidebar.selectbox(
    "Education Level",
    ["BTech", "BCA", "MBA", "Any"]
)

predict_btn = st.sidebar.button("🔮 Recommend Career")

# -------------------------------
# Prediction Logic
# -------------------------------
def generate_roadmap(career):
    roadmap_dict = {
        "Data Scientist": [
            "Learn Python & Pandas",
            "Master Machine Learning",
            "Work on real datasets",
            "Build portfolio projects"
        ],
        "Software Engineer": [
            "Strengthen DSA",
            "Build Web Applications",
            "Learn Git & GitHub",
            "Practice coding interviews"
        ],
        "Product Manager": [
            "Improve communication",
            "Learn product strategy",
            "Understand UX basics",
            "Work on case studies"
        ]
    }
    return roadmap_dict.get(career, ["Build skills", "Gain experience", "Stay updated"])

# -------------------------------
# Output Section
# -------------------------------
# Convert input to dataframe
input_dict = {
    "interest": interest,
    "education": education
}

input_df = pd.DataFrame([input_dict])

# Encode categorical values
for col in input_df.columns:
    input_df[col] = label_encoder.transform(input_df[col])

# Make sure columns match training
input_df = input_df.reindex(columns=model_columns, fill_value=0)

prediction = model.predict(input_df)[0]

# Fetch salary & demand
        career_info = data[data["career"] == prediction].iloc[0]
        salary = career_info["salary_range"]
        demand = career_info["demand"]

        st.subheader("🎯 Recommended Career")
        st.success(prediction)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💰 Salary Range")
            st.info(salary)

        with col2:
            st.markdown("### 📈 Market Demand")
            st.info(demand)

        # Skill Gap
        required_skills = career_info["skills"].split(", ")
        skill_gap = list(set(required_skills) - set(skills))

        st.markdown("### 🧠 Skill Gap Analysis")
        if skill_gap:
            st.write("You should improve these skills:")
            st.write(skill_gap)
        else:
            st.success("You already have strong skill alignment!")

        # Roadmap
        st.markdown("### 🗺️ Career Roadmap")
        roadmap = generate_roadmap(prediction)
        for step in roadmap:
            st.write("✔", step)

        # Visualization
        st.markdown("### 📊 Salary Comparison")

        salary_data = data.groupby("career").count()["salary_range"]
        st.bar_chart(salary_data)

