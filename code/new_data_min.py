import pandas as pd

# CSV 파일 읽기
file_path = "/Users/an-yohan/Documents/GitHub/BigData_Class/data/new_data.csv"
df = pd.read_csv(file_path)

# 각 칼럼의 최소값 계산
min_values = df.min()

print("Minimum value for each column : ")
print(min_values)