


import sys


input = sys.stdin.readline

group = []

k = int(input())

for _ in range(k) :
    one = int(input())

    if one == 0 :
        group.pop()
    else :
        group.append(one)

print(sum(group))