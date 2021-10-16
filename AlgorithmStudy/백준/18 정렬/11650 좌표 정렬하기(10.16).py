

import sys

input = sys.stdin.readline

n = int(input())
nlist = []

for _ in range(n) :
    x,y = map(int, input().split())
    nlist.append([x,y])

nlist.sort(key = lambda x : (x[0], x[1]))

for x,y in nlist :
    print(x, y)

