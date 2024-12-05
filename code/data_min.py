import pandas as pd

# CSV 파일 읽기
file_path = "/Users/an-yohan/Documents/GitHub/BigData_Class/data/diabetes.csv"
df = pd.read_csv(file_path)

# 각 칼럼의 최소값 계산
min_values = df.min()

print("각 칼럼의 최소값:")
print(min_values)
