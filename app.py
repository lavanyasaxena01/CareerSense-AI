# =====================================
# CareerSense AI - Clean Version
# =====================================

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

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
    font-size: 42px;
    font-weight: bold;
    color: #1f4e79;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title Section
# -------------------------------
st.markdown('<p class="main-title">🚀 CareerSense AI</p>', unsafe_allow_html=True)
st.write("An Intelligent Career Guidance & Skill Recommendation System")

st.divider()

# -------------------------------
# Load Model & Encoders
# -------------------------------
@st.cache_resource
def load_resources():
    model = joblib.load("models/career_model.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    model_columns = joblib.load("models/model_columns.pkl")
    return model, label_encoder, model_columns

model, label_encoder, model_columns = load_resources()

# -------------------------------
# Sidebar Inputs
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

def prepare_input():
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

    return input_df


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
    return roadmap_dict.get(career, [
        "Build relevant technical skills",
        "Work on real-world projects",
        "Create portfolio",
        "Apply for internships"
    ])

# -------------------------------
# Output Section
# -------------------------------

if predict_btn:

    if not skills:
        st.warning("⚠ Please select at least one skill.")
    else:

        input_df = prepare_input()

        prediction_encoded = model.predict(input_df)[0]
        prediction = label_encoder.inverse_transform([prediction_encoded])[0]

        col1, col2 = st.columns([2,1])

        # -------------------------------
        # Career Card
        # -------------------------------
        with col1:
            st.markdown(f"""
            <div class="card">
            <h2>🎯 Recommended Career</h2>
            <h3 style='color:#1f77b4;'>{prediction}</h3>
            </div>
            """, unsafe_allow_html=True)

            # Roadmap
            st.markdown("### 🛣 6-Month Roadmap")
            roadmap = generate_roadmap(prediction)
            for step in roadmap:
                st.write("✔", step)

        # -------------------------------
        # Analytics Section
        # -------------------------------
        with col2:
            st.markdown("### 📊 Skill Strength")

            for skill in skills:
                st.progress(80)

            st.markdown("### 💰 Estimated Salary (India)")
            st.metric("Average Range", "₹8–15 LPA")

        # -------------------------------
        # Career Comparison Chart
        # -------------------------------
        st.markdown("### 📈 Career Match Overview")

        sample_scores = {
            "Data Scientist": 0.85,
            "Software Engineer": 0.75,
            "Product Manager": 0.60,
            "Cyber Security": 0.50
        }

        fig, ax = plt.subplots()
        ax.barh(list(sample_scores.keys()), list(sample_scores.values()))
        st.pyplot(fig)

        # -------------------------------
        # Future Scope Section
        # -------------------------------
        st.markdown("### 🚀 Future Enhancements")
        st.info("""
        - Resume parsing integration  
        - LinkedIn profile analysis  
        - Real-time job market API  
        - AI personality assessment  
        """)
