import sys

n = int(sys.stdin.readline())                                                      #반복문으로 여러 줄 입력받는등 시간초과 문제 방지(input)
                                                                                   #a = sys.stdin.readline()로 입력받으면 개행문자 \n까지 들어와서 조땜
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>1 :
        return Fibonacci(n-1)+Fibonacci(n-2)
    else :
        print("Input n ERR!")

print(Fibonacci(n))