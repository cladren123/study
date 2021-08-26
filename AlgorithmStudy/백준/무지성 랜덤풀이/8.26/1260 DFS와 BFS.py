import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# print(graph)

for i in graph :
    i.sort()

# print(graph)

# dfs
visited1 = [0] * (n+1)
stack = [v]

while stack :
    # print(stack)

    cur = stack.pop()
    if visited1[cur] == 1 :
        continue

    visited1[cur] = 1

    print(cur, end = " ")

    temp = sorted(graph[cur], reverse=True)

    for i in temp :
        if visited1[i] == 0 :
            stack.append(i)


print()

# bfs
que = deque()

visited = [0] * (n+1)
que.append(v)



while que :
    cur = que.popleft()

    if visited[cur] == 1 :
        continue

    visited[cur] = 1

    print(cur, end = " ")

    for i in graph[cur] :
        if visited[i] == 0 :
            que.append(i)






















