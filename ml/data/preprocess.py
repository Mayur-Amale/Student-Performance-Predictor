import pandas as pd

df = pd.read_csv("student_data.csv")

df = df.rename(columns={
    "StudyTimeWeekly": "study_hours",
    "Absences":        "absences",
    "GPA":             "gpa"
})

df["attendance"]    = ((30 - df["absences"]) / 30 * 100).round(1)
df["score"]         = (df["gpa"] / 4.0 * 100).round(2)

df[["study_hours", "attendance", "score"]].dropna().to_csv("student_clean.csv", index=False)
print("Done. Rows saved:", len(df))