import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 읽기
file_path = '/Users/an-yohan/Documents/GitHub/BigData_Class/data/diabetes.csv'
data = pd.read_csv(file_path)

# 2. 데이터 전처리 (0값 처리)
data['Glucose'].replace(0, data['Glucose'].mean(), inplace=True)
data['BMI'].replace(0, data['BMI'].mean(), inplace=True)
data['Insulin'].replace(0, data['Insulin'].median(), inplace=True)


sns.histplot(data['Glucose'], kde=True, color='blue', bins=30)
plt.title('Distribution of Glucose Levels')
plt.xlabel('Glucose')
plt.ylabel('Frequency')
plt.show()
