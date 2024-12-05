# pandas 라이브러리 불러오기
import pandas as pd

# 데이터셋 파일 경로 설정 및 데이터 불러오기
file_path = '/Users/an-yohan/Documents/GitHub/BigData_Class/data/diabetes.csv'
data = pd.read_csv(file_path)

# 데이터의 앞부분 5개 행 출력
data.head()

# 데이터프레임의 정보 확인 (열 이름, 데이터 타입, 결측치 등)
data.info()
