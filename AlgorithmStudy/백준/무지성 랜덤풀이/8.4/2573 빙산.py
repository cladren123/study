import copy
import sys
from collections import deque

input = sys.stdin.readline

# n 은 세로, m 은 가로
n, m = map(int, input().split())

graph = []

for _ in range(n) :
    one = list(map(int, input().split()))
    graph.append(one)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def iceCount(graph) :
    count = 0
    visited = [[0] * m for _ in range(n)]

    que = deque()

    # for i in visited :
    #     print(i)

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] != 0 and visited[i][j] == 0 :
                count += 1
                visited[i][j] = count

                que.append([i,j])

                while que :
                    y,x = que.popleft()

                    for k in range(4) :
                        nexty = y + dy[k]
                        nextx = x + dx[k]

                        if 0 <= nextx < m and 0 <= nexty < n :
                            if visited[nexty][nextx] == 0 and graph[nexty][nextx] != 0:
                                visited[nexty][nextx] = count
                                que.append([nexty, nextx])

    return count

year = 0

while True :
    if iceCount(graph) >= 2 :
        print(year)
        break

    graph1 = copy.deepcopy(graph)
    icount = 0

    for i in range(n) :
        for j in range(m) :
            if graph1[i][j] != 0 :

                for k in range(4) :
                    nexty = i + dy[k]
                    nextx = j + dx[k]

                    if graph[nexty][nextx] == 0 :
                        if graph1[i][j] != 0 :
                            graph1[i][j] -= 1
            elif graph1[i][j] == 0 :
                icount += 1

    if icount == (m*n) :
        print(0)
        break

    year += 1
    graph = graph1

    # print(year)
    # for i in graph :
    #     print(i)
    # print()










