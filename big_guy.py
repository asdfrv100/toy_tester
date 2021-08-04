import sys
import time

people_num = int(input())
input_list =[]
for i in range(people_num):
    dan1, dan2= map(int,sys.stdin.readline().split())
    input_list.append([dan1, dan2])


#print(input_list)
order_list = [1] * people_num
for i in range(people_num-1) :
    for j in range(i,people_num):
        if((input_list[i][0] > input_list[j][0])&(input_list[i][1] > input_list[j][1])):
            order_list[j] +=1
        elif((input_list[i][0] < input_list[j][0])&(input_list[i][1] < input_list[j][1])):
            order_list[i] +=1

for i in order_list:
    print(i,end=' ')


# 틀린 내 답
# import sys
# import time
#
# people_num = int(input())
# input_list =[]
#
#
# STATURE=0
# KG=1
# SEQUENCE=2
# BIGGER_COUNT=3
#
#
# for i in range(people_num) :
#     dan1, dan2 = map(int, sys.stdin.readline().split())
#     input_list.append([dan1,dan2,i,0])
#
# #time check start
# start = time.time()
# ####################
#
# input_list=sorted(input_list,key=lambda input_list: input_list[STATURE]+input_list[KG],reverse=True)
#
# bigger_order=1
# people_stack=0
#
# for i in range(0,people_num) :
#     biggest = [i]
#     if input_list[i][BIGGER_COUNT] != 0:
#         continue
#     for j in range(i+1,people_num):
#         if((input_list[i][STATURE] > input_list[j][STATURE]) & (input_list[i][KG] > input_list[j][KG]) ):
#             pass
#         else :
#             if input_list[j][BIGGER_COUNT] == 0:
#                 biggest += [j]
#     for k in biggest :
#         input_list[k][BIGGER_COUNT]=bigger_order
#     bigger_order += len(biggest)
#
#
#
# input_list=sorted(input_list,key=lambda input_list: input_list[SEQUENCE])
#
# for i in range(people_num):
#     print(input_list[i][BIGGER_COUNT],' ',end='')
#
#
#
# #time check end
# print("\n time :", time.time() - start)