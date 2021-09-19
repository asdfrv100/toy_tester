import sys
import math
import time


M, N = sys.stdin.readline().replace('\n','').split()

start=time.time()

M=int(M)
N=int(N)

Prime_number_list=[2]

if N == 2:
    pass
else :
    for i in range(3,N+1):
        for j in (Prime_number_list):
            if i % j ==0:
                break
            elif Prime_number_list[-1] == j:
                Prime_number_list.append(i)

for i in (Prime_number_list):
    if i >= M:
        print(i)

print(time.time()-start)
#
# for i in range(2,N):

