import sys
from collections import deque

input = sys.stdin.readline


n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,e = map(int, input().split())
    graph[e].append(s)

def bfs(node) :
    visited = [0] * (n+1)

    visited[node] = 1

    que = deque()

    que.append(node)

    while que :
        cur = que.popleft()

        for nextnode in graph[cur] :
            if visited[nextnode] == 0 :
                visited[nextnode] = 1
                que.append(nextnode)

    count = visited.count(1)
    return count

maxnum = 0
result = []

for i in range(1,n+1) :
    num = bfs(i)
    # print(i, num)

    if maxnum < num :
        result = [i]
        maxnum = num
    elif maxnum == num :
        result.append(i)

print(*result)














