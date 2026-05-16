import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset

df = pd.read_csv('datasets/network_logs.csv')

print("\nDATASET:\n")
print(df)

# Select features

X = df[['duration', 'src_bytes', 'dst_bytes']]

# Create AI model

model = IsolationForest(contamination=0.2)

# Train model

model.fit(X)

# Predict anomalies

predictions = model.predict(X)

# Add prediction column

df['prediction'] = predictions

print("\nRESULTS:\n")
print(df)

print("\nNOTE:")
print("1 = Normal Activity")
print("-1 = Threat / Anomaly Detected")