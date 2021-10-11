

import sys

input = sys.stdin.readline

n = int(input())
nlist = []

for _ in range(n) :
    one = int(input())
    nlist.append(one)

nlist.sort()

for i in range(n) :
    print(nlist[i])