import sys
import math

N= int(input())
input_list=[]
for i in range(N):
    x1, y1, r1, x2, y2, r2 = sys.stdin.readline().split(' ')
    r2=r2.replace('\n','')
    orignal=[x1, y1, r1, x2, y2, r2]
    orignal=list(map(int,orignal))
    input_list.append(orignal)

for i in range(N):
    x1, y1, r1, x2, y2, r2 = input_list[i]
    origin_len=math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    sub_r1_r2=abs(r1-r2)

    if origin_len==0:
        if ((x1==x2)&(y1==y2))&(r1==r2) :
             print(-1)
        elif((x1==x2)&(y1==y2))&(r1!=r2) :
             print(0)
    elif origin_len !=0:
        if sub_r1_r2+origin_len > max(r1,r2):
            print(1)

        elif origin_len >sub_r1_r2 :
            if (origin_len == float(r1 + r2)):
                print(1)
            elif (origin_len > float(r1 + r2)):
                print(0)
            elif (origin_len < float(r1 + r2)) & (origin_len < sub_r1_r2):
                print(0)
            else:
                print(2)

