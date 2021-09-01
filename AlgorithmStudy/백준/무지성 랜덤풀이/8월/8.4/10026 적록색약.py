"""
BFS & DFS

"""



import copy
import sys

# 빨강과 초록을 같은 걸로 본다.
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n) :
    one = list(input().rstrip())
    graph.append(one)

# for i in graph :
#     print(i)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

que = deque()

# for i in visited :
#     print(i)

graph1 = copy.deepcopy(graph)

for i in range(n) :
    for j in range(n) :
        if graph1[i][j] == 'G' :
            graph1[i][j] = 'R'

# for i in graph1 :
#     print(i)



def check(graph) :
    count = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 :
                count += 1
                visited[i][j] = count
                que.append([i,j])

                while que :
                    y,x = que.popleft()

                    for k in range(4) :
                        nexty = y + dy[k]
                        nextx = x + dx[k]

                        if 0 <= nextx < n and 0 <= nexty < n :
                            if visited[nexty][nextx] == 0 :
                                if graph[y][x] == graph[nexty][nextx] :
                                    visited[nexty][nextx] = count
                                    que.append([nexty, nextx])

    return count


print(check(graph), check(graph1))




















