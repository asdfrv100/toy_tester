import pandas as pd
import numpy as np

#파일명 입력
file_name = 'hashmap.txt'

#파일 행 수 체크
rawdata = pd.read_csv('./onlyinterpol/' +file_name,
sep = "\t", engine = 'python', encoding = "cp949", header = None)

#X, Y 최대 좌표 입력
maxX = int(np.max(rawdata.iloc[:, 0]))
maxY = int(np.max(rawdata.iloc[:, 1]))


#수집한 데이터 넣어놓을 행렬
magx = np.empty((maxX+1, maxY+1))
magy = np.empty((maxX+1, maxY+1))
magz = np.empty((maxX+1, maxY+1))

magx.fill(0)
magy.fill(0)
magz.fill(0)

#수집한 데이터 행렬에 넣기
for i in range(rawdata[0].size):
    magx[int(rawdata.iloc[i, 0]), int(rawdata.iloc[i, 1])] = rawdata.iloc[i, 2]
    magy[int(rawdata.iloc[i, 0]), int(rawdata.iloc[i, 1])] = rawdata.iloc[i, 3]
    magz[int(rawdata.iloc[i, 0]), int(rawdata.iloc[i, 1])] = rawdata.iloc[i, 4]