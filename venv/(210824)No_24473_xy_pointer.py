#11650

import sys
import math
import time

N = int(input())

point_list=[]
for i in range(N):
    x, y = sys.stdin.readline().split(' ')
    x=int(x)
    y=int(y.replace('\n',''))
    point_list.append([x, y])

start_time=time.time()


point_list=sorted(point_list)


for i in range(N):
    print(point_list[i][0],end=' ')
    print(point_list[i][1])

end_time=time.time()-start_time

print(end_time)