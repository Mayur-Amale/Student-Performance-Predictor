import pandas as pd

df = pd.read_csv("student_performance.csv")

# Rename Kaggle columns
df = df.rename(columns={
    "StudyTimeWeekly": "study_hours",
    "Absences":        "absences",
    "GPA":             "gpa"
})

# Derive attendance from absences (0 absences = 100%, 30 absences = 0%)
df["attendance"] = ((30 - df["absences"]) / 30 * 100).round(1)

# Convert GPA (0–4) to score (0–100)
df["score"] = (df["gpa"] / 4.0 * 100).round(2)

# Generate sleep_hours (not in Kaggle dataset — realistic synthetic column)
import numpy as np
np.random.seed(42)
df["sleep_hours"] = np.random.uniform(4, 9, len(df)).round(1)

# Use ParentalSupport as proxy for previous_marks (scale 0–4 → 0–100)
df["previous_marks"] = (df["ParentalSupport"] / 4.0 * 100).round(1)

# Select final 4 features + target
features = ["study_hours", "attendance", "sleep_hours", "previous_marks"]
df_clean = df[features + ["score"]].dropna()

df_clean.to_csv("student_clean.csv", index=False)
print("Saved student_clean.csv —", len(df_clean), "rows")
print(df_clean.describe().round(2))
