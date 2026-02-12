import os, joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
model_path = os.path.join(BASE_DIR, "career_model.pkl")
encoder_path = os.path.join(BASE_DIR, "label_encoder.pkl")
columns_path = os.path.join(BASE_DIR, "model_columns.pkl")

# Load
model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)
model_columns = joblib.load(columns_path)
