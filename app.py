import joblib

model = joblib.load("models/career_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")
model_columns = joblib.load("models/model_columns.pkl")

