# ==========================================================
# PANDAS COMPLETE BASICS
# ==========================================================

import pandas as pd
import numpy as np

# ==========================================================
# 1. SERIES
# ==========================================================

series = pd.Series([10, 20, 30, 40])
print(series)

# ==========================================================
# 2. DATAFRAME CREATION
# ==========================================================

data = {
    "Name": ["Ali", "John", "Sara"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)

# ==========================================================
# 3. DATAFRAME INFORMATION
# ==========================================================

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.info())
print(df.describe())

# ==========================================================
# 4. HEAD & TAIL
# ==========================================================

print(df.head())
print(df.tail())

# ==========================================================
# 5. COLUMN SELECTION
# ==========================================================

print(df["Name"])

print(df[["Name", "Marks"]])

# ==========================================================
# 6. ROW SELECTION
# ==========================================================

print(df.iloc[0])

print(df.iloc[0:2])

print(df.loc[0])

# ==========================================================
# 7. FILTERING
# ==========================================================

print(df[df["Marks"] > 85])

print(df[(df["Age"] > 20) & (df["Marks"] > 85)])

# ==========================================================
# 8. SORTING
# ==========================================================

print(df.sort_values("Marks"))

print(df.sort_values("Marks", ascending=False))

# ==========================================================
# 9. ADDING COLUMNS
# ==========================================================

df["Grade"] = ["A", "A+", "A"]

df["Percentage"] = df["Marks"]

print(df)

# ==========================================================
# 10. DROPPING
# ==========================================================

print(df.drop(columns=["Grade"]))

# ==========================================================
# 11. MISSING VALUES
# ==========================================================

df.loc[1, "Marks"] = np.nan

print(df.isnull())

print(df.isnull().sum())

print(df.fillna(0))

print(df.ffill())

print(df.bfill())

# ==========================================================
# 12. STATISTICS
# ==========================================================

print(df.mean(numeric_only=True))

print(df.median(numeric_only=True))

print(df.std(numeric_only=True))

print(df.var(numeric_only=True))

print(df.min())

print(df.max())

print(df.sum(numeric_only=True))

# ==========================================================
# 13. GROUPBY
# ==========================================================

data2 = {
    "Department": ["IT", "IT", "CS", "CS"],
    "Marks": [90, 85, 95, 80]
}

group_df = pd.DataFrame(data2)

print(group_df.groupby("Department").mean())

print(group_df.groupby("Department").max())

print(group_df.groupby("Department").count())

# ==========================================================
# 14. MERGE
# ==========================================================

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ali", "John", "Sara"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [90, 80, 85]
})

print(pd.merge(students, marks, on="ID"))

# ==========================================================
# 15. CONCAT
# ==========================================================

print(pd.concat([students, marks], axis=1))

# ==========================================================
# 16. APPLY
# ==========================================================

students["Name"] = students["Name"].apply(str.upper)

print(students)

# ==========================================================
# 17. MAP
# ==========================================================

students["Name"] = students["Name"].map(lambda x: x.lower())

print(students)

# ==========================================================
# 18. STRING FUNCTIONS
# ==========================================================

print(students["Name"].str.upper())

print(students["Name"].str.len())

print(students["Name"].str.contains("a"))

# ==========================================================
# 19. DATETIME
# ==========================================================

dates = pd.DataFrame({
    "Date": ["2025-01-01", "2025-02-10"]
})

dates["Date"] = pd.to_datetime(dates["Date"])

print(dates["Date"].dt.year)

print(dates["Date"].dt.month)

print(dates["Date"].dt.day)

# ==========================================================
# 20. DUPLICATES
# ==========================================================

print(students.duplicated())

print(students.drop_duplicates())

# ==========================================================
# 21. PIVOT TABLE
# ==========================================================

sales = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai"],
    "Sales": [100, 200, 150]
})

pivot = pd.pivot_table(
    sales,
    values="Sales",
    index="City",
    aggfunc="sum"
)

print(pivot)

# ==========================================================
# 22. FILE HANDLING
# ==========================================================

# Read CSV
# pd.read_csv("file.csv")

# Read Excel
# pd.read_excel("file.xlsx")

# Save CSV
# df.to_csv("output.csv", index=False)

# Save Excel
# df.to_excel("output.xlsx", index=False)

# ==========================================================
# END OF PANDAS BASICS
# ==========================================================