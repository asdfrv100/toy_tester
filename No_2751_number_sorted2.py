import sys

max_number = int(input())

number_set=set([])
for i in range(max_number):
    number=int(sys.stdin.readline())
    number_set.add(number)

number_set=sorted(number_set)
number_list=list(number_set)
for i in range(len(number_list)):
    print(number_list[i])