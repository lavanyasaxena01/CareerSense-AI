import streamlit as st
import os
import joblib
import pandas as pd

st.set_page_config(page_title="CareerSense AI", layout="wide")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #1f3c88, #39a0ca);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}

/* Cards */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    color: black;
}

/* Buttons */
.stButton>button {
    background-color: #4F46E5;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.stButton>button:hover {
    background-color: #4338CA;
}

/* Titles */
.main-title {
    font-size: 40px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
st.sidebar.title("🚀 CareerSense AI")
st.sidebar.markdown("### Navigation")
st.sidebar.write("🏠 Dashboard")
st.sidebar.write("🔍 Explore Careers")
st.sidebar.write("📊 Skill Analysis")
st.sidebar.write("💬 AI Assistant")

# -------------------- HEADER --------------------
st.markdown('<div class="main-title">🎓 Career Dashboard</div>', unsafe_allow_html=True)
st.markdown("AI-Powered Career Intelligence System")

st.markdown("---")

# -------------------- METRIC CARDS --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Recommended Career", "Data Scientist", "+ High Demand")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Salary Range", "8–15 LPA", "↑ 12% growth")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Job Demand", "High", "🔥 Trending")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(" ")

# -------------------- SKILL GAP SECTION --------------------
st.subheader("📊 Skill Gap Analysis")

col4, col5 = st.columns([2,1])

with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### Your Skill Strength")

    st.progress(80, text="Python")
    st.progress(60, text="Machine Learning")
    st.progress(40, text="SQL")
    st.progress(30, text="Deep Learning")

    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### Improvement Needed")

    st.info("• Deep Learning")
    st.info("• System Design")
    st.info("• Advanced SQL")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(" ")

# -------------------- AI ROADMAP SECTION --------------------
st.subheader("🧠 6-Month AI Roadmap")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("""
**Month 1–2:** Python + SQL  
**Month 3–4:** Machine Learning Projects  
**Month 5:** Internship Preparation  
**Month 6:** Build Portfolio + Apply  
""")

st.markdown('</div>', unsafe_allow_html=True)
