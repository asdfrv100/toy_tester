import sys
import math

number = int(input())
inputed_list=[]
for i in range(number):
    dan1 =int(sys.stdin.readline())
    inputed_list.append(dan1)


sorted_list=sorted(inputed_list,reverse=False)

for i in range(number):
    print(sorted_list[i])
