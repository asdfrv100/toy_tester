

#내 답
import sys
import math
import time

#n = int(sys.stdin.readline())
n = int(input())

start = time.time()


if n == 1 :
    print(2)
else :
    for i in range(1,n) :
        result=0
        sum=0
        target=math.floor(math.log(i, 10))+1
        for j in range(0,target) :
             sum = sum + int((i/(10**j)) % 10)
        sum = i + sum
        if(sum==n) :
            result=sum
            break


print(result)

print("time :", time.time() - start)

#



#
# #정답
# import sys
# import math
# import time
#
# #n = int(sys.stdin.readline())
# n = int(input())
#
# start = time.time()
#
# max_size_count = math.log(n,10)
#
# if n > 18:
#     start_point = n-(math.floor(max_size_count)+1)*9
# else :
#     start_point = 1
#
# if n == 1 :
#     print(2)
# else :
#     for i in range(start_point,n+1) :
#         sum=0
#         target=math.floor(math.log(i, 10))+1
#         for j in range(0,target) :
#              sum = sum + int((i/(10**j)) % 10)
#         sum = i + sum
#         if(sum==n) :
#             print(i)
#             break
#         elif(i==n):
#             print(0)
#
# print("time :", time.time() - start)
#
