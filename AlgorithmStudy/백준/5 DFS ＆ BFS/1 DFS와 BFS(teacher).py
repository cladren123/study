
# n 정점의 개수, m 간선의 개수, v 시작할 정점의 번호
from collections import deque

n, m, v = map(int, input().split())

# n+1 2차원 배열 생성
graph = [[0] * (n+1) for _ in range(n+1)]

# 그래프에 간선을 입히는 과정
for _ in range(m) :
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

# 판을 먼저 깐 다음 내용물들을 넣는다.

visited = [0] * (n+1)

def dfs(node) :
    global n, graph
    visited[node] = 1
    print(node, end = " ")
    for i in range(1, n+1) :
        if graph[node][i] == 1 and visited[i] == 0 :
            dfs(i)

dfs(v)
print()

# bfs 1번

visited1 = [-1] * (n+1)
queue = deque()
queue.append(v)
visited1[v] = 0

while queue :
    cur = queue.popleft()
    print(cur, end = " ")

    for i in range(1, n+1) :
        if graph[cur][i] == 1 and visited1[i] == -1 :
            queue.append(i)
            visited1[i] = visited1[cur] + 1

# print(visited[1:])

# bfs 2번

visited2 = [0] * (n+1)

queue1 = deque()
queue1.append((3,0))
visited2[v] = 1

while queue1 :
    cur = queue1.popleft()   # (node, depth)
    print(cur, end = ' ')

    for i in range(1, n+1) :
        if graph[cur[0]][i] == 1 and visited2[i] == 0 :
            queue1.append((i, cur[i] + 1))
            visited2[i] = 1



