#padnas 불러오기
import pandas as pd

#나의 데이터셋 불어로기
file_path = '/Users/an-yohan/Documents/GitHub/BigData_Class/data/diabetes.csv'
data = pd.read_csv(file_path)

#데이터의 앞부분만 출력하기
data.head()

data.info()