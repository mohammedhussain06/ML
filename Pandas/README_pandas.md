# Pandas Cheat Sheet 🐼

> **Pandas** is an open-source Python library used for data manipulation, cleaning, analysis, and visualization preparation. It provides powerful data structures like **Series** and **DataFrame**, making it the backbone of Data Analysis, EDA, and Machine Learning.

---

# Why Pandas?

- Fast and efficient data manipulation
- Handles structured/tabular data
- Supports missing value handling
- Built-in statistical functions
- Easy data filtering and grouping
- Reads/Writes multiple file formats
- Works seamlessly with NumPy, Matplotlib, Seaborn, and Scikit-Learn

---

# Installation

```bash
pip install pandas
```

```python
import pandas as pd
```

---

# Core Data Structures

## 1. Series

One-dimensional labeled array.

```python
s = pd.Series([10,20,30])
```

---

## 2. DataFrame

Two-dimensional table with rows and columns.

```python
df = pd.DataFrame({
    "Name":["Ali","John"],
    "Age":[20,21]
})
```

---

# Creating DataFrames

| Function | Purpose |
|----------|---------|
| `pd.DataFrame()` | Create DataFrame |
| `pd.Series()` | Create Series |
| `pd.read_csv()` | Read CSV |
| `pd.read_excel()` | Read Excel |
| `pd.read_json()` | Read JSON |
| `pd.read_sql()` | Read SQL Database |

---

# DataFrame Information

| Function | Purpose |
|----------|---------|
| `head()` | First rows |
| `tail()` | Last rows |
| `info()` | Summary |
| `describe()` | Statistics |
| `shape` | Rows × Columns |
| `columns` | Column names |
| `index` | Row labels |
| `dtypes` | Data types |

Example

```python
df.head()
df.info()
df.describe()
```

---

# Selecting Data

## Columns

```python
df["Name"]

df[["Name","Age"]]
```

## Rows

```python
df.iloc[0]

df.iloc[0:5]

df.loc[0]
```

---

# Filtering Data

```python
df[df["Age"]>20]

df[df["Marks"]>=80]

df[(df["Age"]>20)&(df["Marks"]>85)]

df[(df["Age"]<22)|(df["Marks"]>90)]
```

---

# Sorting

```python
df.sort_values("Marks")

df.sort_values("Marks",ascending=False)

df.sort_index()
```

---

# Adding Columns

```python
df["Grade"]="A"

df["Percentage"]=df["Marks"]
```

---

# Removing Data

```python
df.drop("Age",axis=1)

df.drop(columns=["Age"])

df.drop(index=0)
```

---

# Missing Values

| Function | Purpose |
|----------|---------|
| `isnull()` | Detect missing values |
| `notnull()` | Detect valid values |
| `dropna()` | Remove missing values |
| `fillna()` | Fill missing values |
| `ffill()` | Forward Fill |
| `bfill()` | Backward Fill |

Example

```python
df.isnull()

df.fillna(0)

df.dropna()
```

---

# Statistics

```python
df.mean()

df.median()

df.mode()

df.std()

df.var()

df.sum()

df.min()

df.max()

df.count()

df.corr()
```

---

# GroupBy

Used to split, aggregate, and analyze data.

```python
df.groupby("Department").mean()

df.groupby("Department").sum()

df.groupby("Department").count()
```

---

# Merge, Join & Concat

## Merge

```python
pd.merge(df1,df2,on="ID")
```

## Join

```python
df1.join(df2)
```

## Concat

```python
pd.concat([df1,df2])
```

---

# Apply, Map & Lambda

```python
df["Marks"].apply(lambda x:x+5)

df["Name"].map(str.upper)
```

---

# String Operations

```python
df["Name"].str.upper()

df["Name"].str.lower()

df["Name"].str.contains("A")

df["Name"].str.len()

df["Name"].str.replace("A","B")
```

---

# Datetime

```python
df["Date"]=pd.to_datetime(df["Date"])

df["Date"].dt.year

df["Date"].dt.month

df["Date"].dt.day

df["Date"].dt.weekday
```

---

# Duplicate Handling

```python
df.duplicated()

df.drop_duplicates()
```

---

# Pivot Table

```python
pd.pivot_table(
    df,
    values="Sales",
    index="City",
    aggfunc="sum"
)
```

---

# File Handling

## Read Files

```python
pd.read_csv()

pd.read_excel()

pd.read_json()

pd.read_sql()
```

## Save Files

```python
df.to_csv()

df.to_excel()

df.to_json()
```

---

# Useful Functions

```python
value_counts()

unique()

nunique()

sample()

rename()

replace()

astype()

copy()

sort_values()

sort_index()

reset_index()

set_index()
```

---

# Pandas + NumPy

Convert DataFrame to NumPy

```python
df.to_numpy()
```

Convert NumPy to DataFrame

```python
pd.DataFrame(array)
```

---

# Pandas in Machine Learning

Pandas is mainly used for:

- Reading datasets
- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Data Transformation
- Exploratory Data Analysis (EDA)
- Preparing data for Machine Learning

---

# Cheat Sheet Summary

## Creation

```
Series()
DataFrame()
read_csv()
read_excel()
read_json()
```

## Information

```
head()
tail()
info()
describe()
shape
columns
dtypes
```

## Selection

```
loc[]
iloc[]
[]
```

## Filtering

```
>
<
==
&
|
isin()
```

## Statistics

```
mean()
median()
mode()
std()
var()
sum()
min()
max()
corr()
```

## Missing Values

```
isnull()
fillna()
dropna()
ffill()
bfill()
```

## Grouping

```
groupby()
pivot_table()
```

## Combining

```
merge()
join()
concat()
```

## String

```
upper()
lower()
contains()
replace()
len()
```

## Datetime

```
to_datetime()
year
month
day
weekday
```

## File Handling

```
read_csv()
read_excel()
to_csv()
to_excel()
```

---

# Learning Goal 🎯

Master these Pandas fundamentals before moving to:

- ✅ Matplotlib
- ✅ Seaborn
- ✅ Exploratory Data Analysis (EDA)
- ✅ Machine Learning
- ✅ Deep Learning

> **Tip:** If you can comfortably clean, filter, group, merge, and analyze datasets using Pandas without referring to documentation, you're ready to begin Exploratory Data Analysis (EDA) and build end-to-end machine learning pipelines.