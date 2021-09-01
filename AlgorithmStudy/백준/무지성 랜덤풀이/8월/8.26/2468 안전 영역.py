"""

문제 유형 : BFS 와 DFS

visited를 반드시 활용해 방문 여부를 체크한다.
visited를 활용하지 않으면 시간 초과, 메모리 초과가 발생할 수 있다.

"""
import copy
import sys
from collections import deque


input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n) :
    graph.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,-1,0,1]

# BFS 와 DFS 로 풀어보자.

# BFS

def bfs(rain,n,graph1) :
    safezone = 0

    graph = copy.deepcopy(graph1)

    que = deque()

    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] <= rain:
                graph[i][j] = 0

    for i in range(n) :
        for j in range(n) :

            if graph[i][j] > 0 and visited[i][j] == 0 :
                safezone += 1
                que.append([i,j])

                visited[i][j] = 1

                while que :
                    cury, curx = que.popleft()

                    visited[i][j] = 1

                    for k in range(4) :
                        nexty = cury + dy[k]
                        nextx = curx + dx[k]

                        if 0 <= nexty < n and 0 <= nextx < n :
                            if graph[nexty][nextx] > 0 :
                                if visited[nexty][nextx] == 0  :
                                    que.append([nexty, nextx])
                                    visited[nexty][nextx] = 1



    return safezone

height = 0

for i in graph :
    height = max(max(i), height)

# print(height)

answer = 0



for j in range(height) :
    answer = max(bfs(j,n,graph), answer)

print(answer)

