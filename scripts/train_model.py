import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load the cleaned data
df = pd.read_csv('features_clean.csv')

# Split features and labels
X = df.drop(['Dose', 'Time', 'Filename'], axis=1)   # Features
y = df['Dose']                # Labels

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train model
model = XGBClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {acc:.2f}")

# Save model
joblib.dump(model, 'model.pkl')
