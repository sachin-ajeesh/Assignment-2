"""
ABC Company – Employee Data Analysis
-------------------------------------
This script explores an employee dataset to understand:
  1. How the workforce is split across teams and positions
  2. The age distribution of employees
  3. How salary spending breaks down by team and position
  4. Whether there's a relationship between an employee's age and salary

Just point it at your CSV export of the "ABC Company" spreadsheet and run.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# 1. Load the data
# ---------------------------------------------------------------------------
DATA_FILE = "ABC Company.xlsx - Sheet1.csv"

df = pd.read_csv(DATA_FILE)

print("First few rows of the dataset:")
print(df.head())

print("\nColumn info / data types:")
print(df.info())

# ---------------------------------------------------------------------------
# 2. Add a (simulated) Height column
#    The original dataset doesn't include reliable height data, so we
#    generate plausible values (150–180 cm) for demonstration purposes.
#    The fixed seed keeps results reproducible each time the script runs.
# ---------------------------------------------------------------------------
np.random.seed(42)
df["Height"] = np.random.randint(150, 181, size=len(df))

print("\nHeight column (simulated):")
print(df["Height"].head())

# ---------------------------------------------------------------------------
# 3. How are employees distributed across teams?
# ---------------------------------------------------------------------------
team_counts = df["Team"].value_counts()
team_share = round((team_counts / len(df)) * 100, 2)

team_summary = pd.DataFrame({
    "Employee Count": team_counts,
    "Percentage": team_share,
})

print("\nEmployee distribution across teams:")
print(team_summary)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Team", order=team_counts.index)
plt.xticks(rotation=45)
plt.title("Number of Employees per Team")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------
# 4. What positions do employees hold?
# ---------------------------------------------------------------------------
position_counts = df["Position"].value_counts()

print("\nEmployee counts by position:")
print(position_counts)

plt.figure(figsize=(8, 6))
sns.countplot(data=df, y="Position", order=position_counts.index)
plt.title("Employees by Position")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------
# 5. Age distribution, grouped into 5-year bands
# ---------------------------------------------------------------------------
age_bins = [18, 25, 30, 35, 40, 45, 50]
age_labels = ["18-25", "26-30", "31-35", "36-40", "41-45", "46-50"]

df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

age_group_counts = df["Age Group"].value_counts().sort_index()

print("\nEmployees per age group:")
print(age_group_counts)

plt.figure(figsize=(8, 5))
age_group_counts.plot(kind="bar")
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------
# 6. Where is salary being spent? (by team and by position)
# ---------------------------------------------------------------------------
salary_by_team = df.groupby("Team")["Salary"].sum().sort_values(ascending=False)
salary_by_position = df.groupby("Position")["Salary"].sum().sort_values(ascending=False)

print("\nTotal salary spend by team:")
print(salary_by_team)

print("\nTotal salary spend by position:")
print(salary_by_position)

print("\nTeam with the highest salary spend:", salary_by_team.idxmax())
print("Position with the highest salary spend:", salary_by_position.idxmax())

plt.figure(figsize=(10, 5))
salary_by_team.plot(kind="bar")
plt.title("Salary Expenditure by Team")
plt.ylabel("Total Salary")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
salary_by_position.plot(kind="bar")
plt.title("Salary Expenditure by Position")
plt.ylabel("Total Salary")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------
# 7. Is there a relationship between age and salary?
# ---------------------------------------------------------------------------
age_salary_corr = df["Age"].corr(df["Salary"])

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Age", y="Salary")
sns.regplot(data=df, x="Age", y="Salary", scatter=False, color="red")
plt.title("Age vs Salary")
plt.tight_layout()
plt.show()

print("\nCorrelation between Age and Salary:", age_salary_corr)

# ---------------------------------------------------------------------------
# 8. Quick summary
# ---------------------------------------------------------------------------
print("\n--- Summary ---")
print("Total employees:", len(df))
print("Number of teams:", df["Team"].nunique())
print("Number of positions:", df["Position"].nunique())
print("Age–Salary correlation:", age_salary_corr)
