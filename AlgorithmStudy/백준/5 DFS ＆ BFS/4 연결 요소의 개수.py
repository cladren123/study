
n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1) ]

for _ in range(m) :
    u,v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in graph :
    print(i)

