import sys
import numpy as np
import copy
import time



##입력값 list화
row,col = map(int,sys.stdin.readline().split())
original_borad=[]
for i in range(row):
    line = input()
    original_borad.append(line)

start = time.time()


#넘파이 아스키코드로 변환
AS_original_borad=np.empty([0,col], float)
for i in range(row):
    line=np.array([])
    for j in range(col):
        line=np.append(line,(ord(original_borad[i][j])))
    AS_original_borad=np.append(AS_original_borad,np.array([line]),axis=0)


##답지 making
Black_start=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
AS_Black_start=np.empty([0,8], float)
AS_White_start=np.empty([0,8], float)

for i in range(8):
    line=np.array([])
    for j in range(8):
        line=np.append(line,ord(Black_start[i][j]))
    AS_Black_start=np.append(AS_Black_start,np.array([line]),axis=0)

AS_White_start=copy.deepcopy(AS_Black_start)
dummy=  AS_White_start[0]
AS_White_start = np.append(AS_White_start[1:],(AS_White_start[:1]),axis=0)






#후보군 8x8 리스트 생성 후 비교
something_possible_list=np.array([])

min_count=0

for i in range(row-7):
    for j in range(col-7):
        dummy_board = [row[j:j+8] for row in AS_original_borad[i:i+8]]
        Black_sub=dummy_board-AS_Black_start
        White_sub=dummy_board-AS_White_start

        black_key, black_val=np.unique(Black_sub, return_counts=True)
        white_key, white_val=np.unique(White_sub, return_counts=True)


        black_sum=0
        white_sum=0

        for k in range(len(black_key)):
            if black_key[k]!=0.0:
                black_sum+=black_val[k]
        for k in range(len(white_key)):
            if white_key[k]!=0.0:
                white_sum+=white_val[k]

        minimum=min(black_sum,white_sum)

        if (i==0)&(j==0):
            min_count=minimum
        else :
            min_count=min(min_count,minimum)


print(min_count)

print("time :", time.time() - start)