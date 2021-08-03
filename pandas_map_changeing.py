import pandas as pd

# 탭으로 분리된(tsv) .txt 텍스트파일 불러오기
# data = pd.read_csv('파일경로', sep = "\t", , engine='python', encoding = "인코딩방식")
data = pd.read_csv('고객정보.txt', sep = "\t", , engine='python', encoding = "cp949")
data =