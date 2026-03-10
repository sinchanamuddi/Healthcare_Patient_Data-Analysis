import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

# 1. SETUP PATHS - Ensures the file is found even if run from a different folder
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'healthcare_dataset.csv')

# 2. LOAD & INITIAL INSPECTION 
try:
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully!")
    print(df.info())
except FileNotFoundError:
    print(f"Error: Could not find 'healthcare_dataset.csv' at {file_path}")
    sys.exit()

# 3. DATA CLEANING 
# Remove duplicates and handle missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# 4. CATEGORIZE BY AGE GROUPS 
# Creating custom bins to analyze life stages
bins = [0, 12, 19, 35, 60, 100]
labels = ['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 5. ANALYSIS - DISEASE PREVALENCE ACROSS DEMOGRAPHICS [cite: 94, 95]
# Identifying high-risk groups (e.g., disease frequency by age group)
disease_by_age = df.groupby('Age Group')['Medical Condition'].value_counts().unstack()
print("\nDisease Distribution by Age Group:")
print(disease_by_age)

# 6. VISUALIZATION 
plt.figure(figsize=(12, 6))

# Subplot 1: Disease frequency by Gender
plt.subplot(1, 2, 1)
sns.countplot(data=df, x='Medical Condition', hue='Gender', palette='Set2')
plt.title('Disease Frequency by Gender')
plt.xticks(rotation=45)

# Subplot 2: Age Distribution of Patients
plt.subplot(1, 2, 2)
sns.histplot(df['Age'], bins=20, kde=True, color='teal')
plt.title('Age Distribution of Patients')

plt.tight_layout()
plt.show()

# 7. VISUALIZING RISK FACTORS (Boxplot for Billing vs Medical Condition)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Medical Condition', y='Billing Amount', palette='coolwarm')
plt.title('Billing Amount Distribution by Medical Condition')
plt.xticks(rotation=45)
plt.show()