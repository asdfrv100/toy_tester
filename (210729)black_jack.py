N, M = map(int, input().split(' '))
numbers = sorted(list(int(x) for x in input().split()))


answer=0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum=numbers[i]+numbers[j]+numbers[k]
            difference = M - sum
            ans_difference = M - answer
            if (difference >=0) and (difference < ans_difference):
                answer = sum

print(answer)


#range(3,5) = 3,4나옴, range(3)은 앞에 0 생략
# 다수의 입력을 받는 방법 int(x) for x in input().split() ->이걸 list화