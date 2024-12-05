import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 읽기
file_path = '/Users/an-yohan/Documents/GitHub/BigData_Class/data/diabetes.csv'  # 데이터 파일 경로를 확인하세요.
data = pd.read_csv(file_path)

# 2. 데이터 전처리 (0값 처리)
data['Glucose'].replace(0, data['Glucose'].mean(), inplace=True)
data['BMI'].replace(0, data['BMI'].mean(), inplace=True)
data['Insulin'].replace(0, data['Insulin'].median(), inplace=True)

# 3. Insulin 분포 시각화
sns.histplot(data['Insulin'], kde=True, color='green', bins=30)
plt.title('Distribution of Insulin Levels')
plt.xlabel('Insulin')
plt.ylabel('Frequency')
plt.show()
