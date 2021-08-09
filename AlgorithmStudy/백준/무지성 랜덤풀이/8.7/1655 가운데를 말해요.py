import sys

"""
문제유형 : 우선순위 큐 
"""

input = sys.stdin.readline

n = int(input())

slist = []

index = 0

for i in range(1,n+1) :

    one = int(input())

    slist.append(one)

    # 시간 초과 발생
    slist.sort()

    if i % 2 == 1 :
        print(slist[index])
    elif i % 2 == 0 :
        print(slist[index])
        index += 1






