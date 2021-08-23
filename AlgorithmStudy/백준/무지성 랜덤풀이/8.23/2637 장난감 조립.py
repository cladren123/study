"""

문제 유형

"""
import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

gibonx = 101

que = deque()

for _ in range(m) :
    x,y,k = map(int, input().split())
    gibonx = min(gibonx, x)
    graph[x].append([y,k])

    que.append([x,y,k])

gibon = [0] * (gibonx)

for i in graph :
    print(i)

while que :
    x,y,k = que.popleft()

    if x < gibonx :
        gibon[y] += k

    elif x >= gibonx :
        for _ in range()







print(gibon)

