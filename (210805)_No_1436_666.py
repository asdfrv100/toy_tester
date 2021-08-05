import sys
import math
import time




number = int(input())

start = time.time()

count = 0
ripple_digit=6
ripple_count=3

for i in range(666,10001):
    change_num=i
    digit_count=[]
    while change_num>10:
        digit_count.append(change_num%10)
        change_num=change_num//10
    digit_count.append(change_num)

    innercount=0
    while len(digit_count) >0:
        if digit_count[-1] != ripple_digit:
            innercount=0
        else :
            innercount+=1
        del digit_count[-1]
        if innercount==3:
            break
    if innercount >= ripple_count:
        count+=1
    if count == number:
        print(i)
        break

#time check end
print("\n time :", time.time() - start)