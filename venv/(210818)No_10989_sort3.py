import math
import sys
import time



############외부에서 값 입력받음##########################
N = int(input())
count_list=[0]*10001

for i in range(N):
    count_list[int(sys.stdin.readline())]+=1
start = time.time()

######################################
#count list,result_list 만들기

# max_value=max(input_list)


#result_list=[0 for i in range(len(input_list))]
#################################
#step 1- 각 숫자 개수 세줌 - 저장
# for k in input_list:
#     count_list[k-1]+=1

for i in range(10001):
    for j in range(count_list[i]):
        print(i)

print("time :", time.time() - start)
# import math
# import sys
#
#
# ############외부에서 값 입력받음##########################
# N = int(input())
# input_list=[]
#
# for i in range(N):
#     input_list.append(int(sys.stdin.readline()))
#
# ######################################
# #count list,result_list 만들기
#
# max_value=max(input_list)
# count_list=[0 for i in range(10001)]
#
# result_list=[0 for i in range(len(input_list))]
# #################################
# #step 1- 각 숫자 개수 세줌 - 저장
# for k in input_list:
#     count_list[k-1]+=1
#
# #step 2 - 누적합 배열 생성
# for i in range(len(count_list)):
#     if i==0:
#         pass
#     else:
#         count_list[i]+=count_list[i-1]
#
#
# #step 3 - 누적합 배열 정렬
# for i in input_list:
#     result_list[count_list[i-1]-1]=i
#     count_list[i-1]-=1
#
# print(result_list)