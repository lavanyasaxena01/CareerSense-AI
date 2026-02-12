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

import pandas as pd

# Create empty dataframe with all model columns
input_df = pd.DataFrame(columns=model_columns)

# Initialize all values to 0
input_df.loc[0] = 0

# Convert user inputs into dummy format
# Example assumes naming format like "Skills_Python"

# Qualification
qual_col = f"Highest Qualification_{education.lower()}"
if qual_col in input_df.columns:
    input_df.at[0, qual_col] = 1

# Interests (split by comma)
for word in interest.lower().split(","):
    word = word.strip()
    col_name = f"Primary Interests_{word}"
    if col_name in input_df.columns:
        input_df.at[0, col_name] = 1

# Skills (split by comma)
for word in skills.lower().split(","):
    word = word.strip()
    col_name = f"Skills_{word}"
    if col_name in input_df.columns:
        input_df.at[0, col_name] = 1

# Now predict
if predict_btn:

    # Create empty dataframe with training columns
    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    # Convert education
    edu_col = f"Highest Qualification_{education.lower()}"
    if edu_col in input_df.columns:
        input_df.at[0, edu_col] = 1

    # Convert interest
    interest_col = f"Primary Interests_{interest.lower()}"
    if interest_col in input_df.columns:
        input_df.at[0, interest_col] = 1

    # Convert skills
    for skill in skills:
        skill_col = f"Skills_{skill.lower()}"
        if skill_col in input_df.columns:
            input_df.at[0, skill_col] = 1

    # Predict
    prediction_encoded = model.predict(input_df)[0]
    prediction = label_encoder.inverse_transform([prediction_encoded])[0]

    st.subheader("🎯 Recommended Career")
    st.success(prediction)


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

if predict_btn:

    # Create empty dataframe with training columns
    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    # Education
    edu_col = f"Highest Qualification_{education.lower()}"
    if edu_col in input_df.columns:
        input_df.at[0, edu_col] = 1

    # Interest
    interest_col = f"Primary Interests_{interest.lower()}"
    if interest_col in input_df.columns:
        input_df.at[0, interest_col] = 1

    # Skills
    for skill in skills:
        skill_col = f"Skills_{skill.lower()}"
        if skill_col in input_df.columns:
            input_df.at[0, skill_col] = 1

    # Predict
    prediction_encoded = model.predict(input_df)[0]
    prediction = label_encoder.inverse_transform([prediction_encoded])[0]

    st.subheader("🎯 Recommended Career")
    st.success(prediction)

    # OPTIONAL: Salary & Demand (only if you have dataset loaded)
    # data = pd.read_csv("data/careers_dataset.csv")
    # career_info = data[data["career"] == prediction].iloc[0]
    # st.write("Salary:", career_info["salary_range"])
