

import sys

input = sys.stdin.readline

n = int(input())

sdict = dict()

for _ in range(n) :
    str1, str2 = input().strip().split()

    sdict[str1] = str2

# 역순 정렬
sdict = dict(sorted(sdict.items(), reverse=True))


for key,value in sdict.items() :
    if value == 'enter' :
        print(key)


