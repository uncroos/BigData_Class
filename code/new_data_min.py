import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# 데이터 로드 및 요약
data = pd.read_csv('/Users/an-yohan/Documents/GitHub/BigData_Class/data/new_data.csv')
print(data.describe())

data['BMI_Group'] = pd.cut(data['BMI'], bins=[0, 18.5, 25, 30, 100], 
                           labels=['Underweight', 'Normal', 'Overweight', 'Obese'])
grouped = data.groupby('BMI_Group')['Outcome'].mean()
print(grouped)

# 1. BMI 그룹별 당뇨병 발생률 (Barplot)
grouped = data.groupby('BMI_Group')['Outcome'].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped.index, y=grouped.values)
plt.title("BMI Group vs Diabetes Prevalence")
plt.ylabel("Diabetes Prevalence")
plt.show()

# 2. BMI와 혈당의 상관 관계 (Scatterplot)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='BMI', y='Glucose', hue='Outcome', data=data)
plt.title("BMI vs Glucose by Diabetes Outcome")
plt.show()

# 3. BMI와 당뇨병 여부에 따른 체중 분포 (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Outcome', y='BMI', data=data)
plt.title("Weight Distribution by Diabetes Outcome")
plt.show()

# 4. BMI와 혈당의 분포 (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x='BMI', kde=True, color='blue', bins=30)
plt.title("Distribution of BMI")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=data, x='Glucose', kde=True, color='green', bins=30)
plt.title("Distribution of Glucose Levels")
plt.show()

# 5. 변수 간 상관관계 (Heatmap)
corr = data[['BMI', 'Glucose', 'Age', 'BloodPressure', 'Insulin', 'Outcome']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# 6. 비만과 당뇨병 여부에 따른 나이 분포 (Density plot)
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data[data['Outcome'] == 0]['Age'], label='No Diabetes', shade=True)
sns.kdeplot(data=data[data['Outcome'] == 1]['Age'], label='Diabetes', shade=True)
plt.title("Age Distribution by Diabetes Outcome")
plt.legend()
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
data = pd.read_csv('/Users/an-yohan/Documents/GitHub/BigData_Class/data/new_data.csv')

# BMI 그룹 생성
data['BMI_Group'] = pd.cut(data['BMI'], bins=[0, 18.5, 25, 30, 100], 
                           labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

# 1. BMI 그룹별 당뇨병 발생률 (Barplot)
grouped = data.groupby('BMI_Group')['Outcome'].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped.index, y=grouped.values)
plt.title("BMI Group vs Diabetes Prevalence")
plt.ylabel("Diabetes Prevalence")
plt.show()

# 2. BMI와 혈당의 상관 관계 (Scatterplot + Regression Line)
sns.lmplot(x='BMI', y='Glucose', hue='Outcome', data=data, height=6, aspect=1.2)
plt.title("BMI vs Glucose with Regression Line")
plt.show()

# 3. Outcome별 BMI, Glucose 분포 (Violin Plot)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.violinplot(x='Outcome', y='BMI', data=data, palette='muted')
plt.title("BMI Distribution by Outcome")

plt.subplot(1, 2, 2)
sns.violinplot(x='Outcome', y='Glucose', data=data, palette='muted')
plt.title("Glucose Distribution by Outcome")
plt.tight_layout()
plt.show()

# 4. 주요 변수의 Outcome별 평균 (Categorical Heatmap)
mean_values = data.groupby('Outcome').mean().T
plt.figure(figsize=(8, 6))
sns.heatmap(mean_values, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("Mean Values of Variables by Outcome")
plt.show()

# 5. 변수 간 상관관계 (Heatmap)
corr = data[['BMI', 'Glucose', 'Age', 'BloodPressure', 'Insulin', 'Outcome']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# 6. 변수 간 관계 종합 (Pairplot)
sns.pairplot(data[['BMI', 'Glucose', 'Age', 'BloodPressure', 'Outcome']], hue='Outcome', diag_kind='kde', palette='husl')
plt.suptitle("Pairplot of Key Variables", y=1.02)
plt.show()
