import sys
import math

number = int(input())
inputed_list=[]
for i in range(number):
    dan1, dan2 =sys.stdin.readline().replace('\n','').split()
    dan1=int(dan1)
    dan2=int(dan2)
    inputed_list.append([dan2, dan1])

sorted_list=sorted(inputed_list,reverse=False)

for i in range(len(sorted_list)):
    print(sorted_list[i][1],sorted_list[i][0],end='\n')

