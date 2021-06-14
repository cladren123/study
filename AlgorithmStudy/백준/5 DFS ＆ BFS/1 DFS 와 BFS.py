from collections import deque

n, m, start = map(int, input().split())

graph = list(([0] *(n+1)  for i in range(n+1)))

for _ in range(m) :
    s,e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

# dfs에 visited가 있으면 visited가 계속 초기화되면서 답이 안나온다.
visited = [0] * (n+1)

def dfs(node) :
    global n, graph
    global visited
    print(node, end = " ")
    # 여기에서 visited 책정한다.
    visited[node] = 1

    for i in range(1,n+1) :
        if graph[node][i] == 1 and visited[i] == 0 :
            visited[i] = 1
            dfs(i)

def bfs() :
    global n, graph
    visited = [0] * (n+1)

    queue = deque()
    queue.append(start)
    visited[start] = 1


    while queue :
        cur = queue.popleft()
        print(cur, end = " ")
        for i in range(n+1) :
            if graph[cur][i] == 1 and visited[i] == 0 :
                queue.append(i)
                visited[i] = 1

dfs(start)
print()
bfs()




