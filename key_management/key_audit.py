import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import json

MODEL_PATH = "/content/FortiCryptX-Colab/key_management/anomaly_model.pkl"

def train_anomaly_model(log_file):
    rows = []
    with open(log_file, 'r') as f:
        for line in f:
            try:
                obj = json.loads(line.strip())
                if 'details' in obj:
                    rows.append(obj['details'])
            except json.JSONDecodeError:
                print(f"[!] Skipping bad line: {line.strip()}")
    
    df = pd.DataFrame(rows)
    
    # Ensure required columns exist
    if not all(col in df.columns for col in ['file_size', 'duration', 'key_size']):
        raise ValueError("Missing required fields (file_size, duration, key_size) in logs.")

    model = IsolationForest(contamination=0.05)
    model.fit(df[['file_size', 'duration', 'key_size']])
    joblib.dump(model, MODEL_PATH)


def detect_anomaly(log_file):
    model = joblib.load(MODEL_PATH)
    rows = []
    with open(log_file, 'r') as f:
        for line in f:
            try:
                obj = json.loads(line.strip())
                if 'details' in obj:
                    rows.append(obj['details'])
            except json.JSONDecodeError:
                continue
    
    df = pd.DataFrame(rows)
    preds = model.predict(df[['file_size', 'duration', 'key_size']])
    df['anomaly'] = preds
    return df[df['anomaly'] == -1]
