import sys
import math
import time
import copy

number = int(input())

start = time.time()

num_666_list=[666,6660]

reverse_candi_num = []
for i in range(1,2800):
    num = i
    digit_num = []
    while num > 10 :
        digit_num.append(str(num%10))
        num=num//10
    digit_num.append(copy.deepcopy(num))
    print(digit_num)


    if len(reverse_digit_num) != 1:
        digit_num=reversed(reverse_digit_num)
    else :
        digit_num=copy.deepcopy(reverse_digit_num)
    print(type(digit_num))
    str_new_num=[]
    for j in range(len(digit_num)+1):
        str_new_num=copy.deepcopy(digit_num)
        str_new_num.insert(j, '666')
#        print(type(str_new_num))
        new=''
        for k in range(len(str_new_num)):
            new=new+str_new_num[k]
        new_int=int(new)
        num_666_list.append(new_int)

num_666_list = sorted(num_666_list,revers=False)

print(num_666_list[number+1])

#틀린 답
# import sys
# import math
# import time
#
#
#
#
# number = int(input())
#
# start = time.time()
#
# count = 0
# ripple_digit=6
# ripple_count=3
#
# for i in range(666,10000):
#     change_num=i
#     digit_count=[]
#     while change_num>10:
#         digit_count.append(change_num%10)
#         change_num=change_num//10
#     digit_count.append(change_num)
#
#     innercount=0
#     while len(digit_count) >0:
#         if digit_count[-1] != ripple_digit:
#             innercount=0
#         else :
#             innercount+=1
#         del digit_count[-1]
#         if innercount==3:
#             break
#     if innercount >= ripple_count:
#         count+=1
#     if count == number:
#         print(i)
#         break
#
#
# #time check end
# print("\n time :", time.time() - start)