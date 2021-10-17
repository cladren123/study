

import sys

input = sys.stdin.readline

n = int(input())
nlist = []

for _ in range(n) :
    x,y = map(int, input().split())
    nlist.append([x,y])

# y, x 순서로 중렬
nlist.sort(key = lambda x : (x[1], x[0]))

for i in nlist :
    print(*i)