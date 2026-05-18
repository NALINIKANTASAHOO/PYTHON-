import pandas as pd
df = pd.read_csv("student_data.csv")
print(df)
# Load dataset
df = pd.read_csv("student_data.csv")

# Show first rows
print(df.head())

# Average scores
print("\nAverage Scores:")
print(df[['Math_Score','Science_Score','English_Score']].mean())

# Pass/Fail count
print("\nResult Count:")
print(df['Final_Result'].value_counts())

# Correlation
print("\nCorrelation:")
print(df.corr(numeric_only=True))
print(df.info())
print(df.describe())
print(df.describe(include='all'))
