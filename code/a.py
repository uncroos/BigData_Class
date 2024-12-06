import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# 한글 폰트 설정 (OS에 맞게 설정)
mpl.rcParams['font.family'] = 'AppleGothic'  # Mac
# 음수 기호 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

# 데이터 로드 및 요약
data = pd.read_csv('/Users/an-yohan/Documents/GitHub/BigData_Class/data/new_data.csv')
print(data.describe())

# 1. Glucose vs Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data, x='Glucose', hue='Outcome', fill=True, palette='husl', alpha=0.5)
plt.title('Outcome에 따른 Glucose 분포')
plt.xlabel('Glucose (혈당)')
plt.ylabel('밀도')
plt.show()

# 2. BMI vs Glucose (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='BMI', y='Glucose', hue='Outcome', palette='husl')
plt.title('Outcome에 따른 BMI와 Glucose의 관계')
plt.xlabel('BMI (체질량지수)')
plt.ylabel('Glucose (혈당)')
plt.show()

# 3. Age vs Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data, x='Age', hue='Outcome', fill=True, palette='husl', alpha=0.5)
plt.title('Outcome에 따른 Age 분포')
plt.xlabel('Age (나이)')
plt.ylabel('밀도')
plt.show()

# 4. BMI vs Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=data, x='BMI', hue='Outcome', fill=True, palette='husl', alpha=0.5)
plt.title('Outcome에 따른 BMI 분포')
plt.xlabel('BMI (체질량지수)')
plt.ylabel('밀도')
plt.show()
