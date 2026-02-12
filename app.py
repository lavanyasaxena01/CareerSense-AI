import streamlit as st
import joblib
import os

st.set_page_config(page_title="CareerSense AI", layout="centered")

st.title("🎯 CareerSense AI")
st.write("If you can see this, the app is working!")

# --- DEBUGGING: Check if files exist ---
st.sidebar.header("System Status")
files = ['career_model.pkl', 'label_encoder.pkl', 'model_columns.pkl']
missing_files = []

for f in files:
    if os.path.exists(f):
        st.sidebar.success(f"✅ Found {f}")
    else:
        st.sidebar.error(f"❌ Missing {f}")
        missing_files.append(f)

if missing_files:
    st.error(f"The app cannot start because these files are missing: {missing_files}")
    st.stop()

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
