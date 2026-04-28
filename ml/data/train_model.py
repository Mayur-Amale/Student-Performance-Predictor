import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("student_clean.csv")

FEATURES = ["study_hours", "attendance", "sleep_hours", "previous_marks"]
X = df[FEATURES]
y = df["score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Random Forest ---
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)
rf_r2  = r2_score(y_test, rf_preds)
rf_mae = mean_absolute_error(y_test, rf_preds)

print("Random Forest:")
print(f"  R2  : {rf_r2:.4f}")
print(f"  MAE : {rf_mae:.2f}")

# --- Linear Regression ---
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)
lr_r2  = r2_score(y_test, lr_preds)
lr_mae = mean_absolute_error(y_test, lr_preds)

print("\nLinear Regression:")
print(f"  R2  : {lr_r2:.4f}")
print(f"  MAE : {lr_mae:.2f}")

# --- Pick best model ---
if rf_r2 >= lr_r2:
    best_model = rf
    best_name  = "RandomForest"
else:
    best_model = lr
    best_name  = "LinearRegression"

print(f"\n✅ Best model: {best_name} (R2={max(rf_r2, lr_r2):.4f})")

pickle.dump(best_model, open("model.pkl", "wb"))
print("model.pkl saved ✓")
