
"""

문제 유형 : DFS, BFS

"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

# BFS, DFS 2가지의 방법으로 풀어보자.

# BFS 너비 우선 탐색

que = deque()
parents1 = [0] * (n+1)

que.append(1)

while que :
    cur = que.popleft()

    for i in graph[cur] :
        if parents1[i] == 0 :
            que.append(i)
            parents1[i] = cur

# for i in range(2, n+1) :
#     print(parents1[i])


# DFS

stack = []
parents2 = [0] * (n+1)

stack.append(1)

while stack :
    cur = stack.pop()

    temp = sorted(graph[cur], reverse=True)

    for i in temp :
        if parents2[i] == 0 :
            stack.append(i)
            parents2[i] = cur

for i in range(2, n+1) :
    print(parents2[i])

















