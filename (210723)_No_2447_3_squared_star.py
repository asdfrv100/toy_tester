import sys

n = int(sys.stdin.readline())

def squared_3_star(n,m):
    if n == 0:
        print("*",end=' ')
    else :
        for i in range(3**m):
            squared_3_star((n-1),m)
            squared_3_star((n-1),m)
            squared_3_star((n-1),m)
            if(n==m):
                print('')



print(squared_3_star(n,n))
