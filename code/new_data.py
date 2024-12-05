import pandas as pd

# CSV 파일 읽기
file_path = "/Users/an-yohan/Documents/GitHub/BigData_Class/data/diabetes.csv"
df = pd.read_csv(file_path)

# 0값을 평균값으로 대체
columns_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for column in columns_to_fix:
    # 0을 NaN으로 바꾼 후 평균값으로 대체
    df[column] = df[column].replace(0, pd.NA)
    df[column] = df[column].fillna(df[column].mean())

# 새로운 CSV 파일로 저장
new_file_path = "new_data.csv"
df.to_csv(new_file_path, index=False)

print(f"처리된 데이터가 '{new_file_path}'에 저장되었습니다.")
