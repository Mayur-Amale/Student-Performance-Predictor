import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Load data
df = pd.read_csv("student_clean.csv")

# Validate columns
required_cols = ["study_hours", "attendance", "score"]
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# Features & Target
X = df[["study_hours", "attendance"]]
y = df["score"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------- Model 1: Random Forest --------
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

rf_preds = rf.predict(X_test)

print("\nRandom Forest:")
print(f"R2 Score : {r2_score(y_test, rf_preds):.4f}")
print(f"MAE      : {mean_absolute_error(y_test, rf_preds):.2f}")

# -------- Model 2: Linear Regression --------
lr = LinearRegression()
lr.fit(X_train, y_train)

lr_preds = lr.predict(X_test)

print("\nLinear Regression:")
print(f"R2 Score : {r2_score(y_test, lr_preds):.4f}")
print(f"MAE      : {mean_absolute_error(y_test, lr_preds):.2f}")

# Choose best model (manual for now)
model = 

# Save model with metadata
model_data = {
    "model": model,
    "features": X.columns.tolist()
}

pickle.dump(model_data, open("model.pkl", "wb"))

print("\nModel saved as model.pkl")