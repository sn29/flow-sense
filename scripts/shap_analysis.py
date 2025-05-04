import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Use non-interactive mode
import matplotlib
matplotlib.use('Agg')

# Load model and features
print(f"📂 Working in: {os.getcwd()}")
model = joblib.load("model.pkl")
df = pd.read_csv("features_clean.csv")

# Drop metadata columns
X = df.drop(['Dose', 'Time', 'Filename'], axis=1)

# SHAP with XGBoost (native support)
explainer = shap.Explainer(model)
shap_values = explainer(X)

# Mean SHAP value per feature
mean_shap = np.abs(shap_values.values).mean(axis=0)
shap_series = pd.Series(mean_shap, index=X.columns).sort_values(ascending=True)

# Plot
plt.figure(figsize=(8, 6))
shap_series.plot(kind='barh')
plt.title("Mean Absolute SHAP Values (XGBoost)")
plt.xlabel("SHAP Value (impact on prediction)")
plt.tight_layout()
plt.savefig("shap_summary.png", bbox_inches='tight')
print("✅ SHAP summary saved as shap_summary.png")
