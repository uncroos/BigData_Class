import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
data = pd.read_csv('/Users/an-yohan/Documents/GitHub/BigData_Class/data/new_data.csv')


# 1. Glucose vs Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data, x='Glucose', hue='Outcome', fill=True, palette='husl', alpha=0.5)
plt.title('Distribution of Glucose by Outcome')
plt.xlabel('Glucose')
plt.ylabel('Density')
plt.show()

# 2. BMI vs Glucose (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='BMI', y='Glucose', hue='Outcome', palette='husl')
plt.title('BMI vs Glucose by Outcome')
plt.xlabel('BMI')
plt.ylabel('Glucose')
plt.show()

# 3. Age vs Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data, x='Age', hue='Outcome', fill=True, palette='husl', alpha=0.5)
plt.title('Distribution of Age by Outcome')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

# 4. BMI vs Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data, x='BMI', hue='Outcome', fill=True, palette='husl', alpha=0.5)
plt.title('Distribution of BMI by Outcome')
plt.xlabel('BMI')
plt.ylabel('Density')
plt.show()
