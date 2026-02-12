import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "career_model.pkl")
encoder_path = os.path.join(BASE_DIR, "label_encoder.pkl")
columns_path = os.path.join(BASE_DIR, "model_columns.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)
model_columns = joblib.load(columns_path)
