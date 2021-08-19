import sys
import math

N = input()

#print(len(N))

digit=[]
#자르기
for i in range(len(N)):
    digit.append(N[i:i+1])
#print(digit)
#정렬
digit.sort(reverse=True)

#합치기
digit_join="".join(digit)

print(digit_join)

#1위 답안

#print(''.join(sorted(input())[ : :-1]))
#step