import sys

N = int(input())

input_list=[]

for i in range(0,N):
    dan = int(sys.stdin.readline().replace('\n','').split())
    input_list.append(dan)


#산술평균 - 첫째 자리 반올림
add_result=sum(input_list)

print(int(round(add_result/len(input_list),0)))

#중앙값

middle_list=sorted(input_list)

print(middle_list[int(round(len(middle_list)/2))])