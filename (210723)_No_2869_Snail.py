# #a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# #리턴값: a에 포함되어 있는 정수 n개의 합 (정수)0
import sys

a, b, v = map(int, sys.stdin.readline().split())

def climing(A,B,V):
    if(A >= V):
        return 1
    else:
        count=((V-A) / (A-B))
        others=((V-A) % (A-B))
        if others > 0:
            return int(count+2)
        else:
            return int(count+1)

        #ceil써보기

print(climing(a, b, v))
