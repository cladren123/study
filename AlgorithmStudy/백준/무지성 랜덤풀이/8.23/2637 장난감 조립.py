"""

문제 유형 : 다이나믹프로그래밍, 그래프 이론, 위상 정렬



메모리 초과 발생

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

    if x == n :
        que.append([y,k])

gibon = [0] * (gibonx)


while que :
    y,k = que.popleft()

    if y < gibonx :
        gibon[y] += k

    elif y >= gibonx :
        for _ in range(k) :
            for i in graph[y] :
                que.append([i[0], i[1]])



for i in range(1,gibonx) :
    print("%d %d" %(i, gibon[i]))

"""
import sys
from collections import deque, defaultdict

input = sys.stdin.readline


n = int(input())
m = int(input())

graph = defaultdict(list)

gibonx = 101

que = deque()

for _ in range(m) :
    x,y,k = map(int, input().split())
    gibonx = min(gibonx, x)
    graph[x].append([y,k])

    if x == n :
        que.append([y,k])

gibon = [0] * (gibonx)


while que :
    y,k = que.popleft()

    if y < gibonx :
        gibon[y] += k

    elif y >= gibonx :
        for _ in range(k) :
            for i in graph[y] :
                que.append([i[0], i[1]])



for i in range(1,gibonx) :
    print("%d %d" %(i, gibon[i]))