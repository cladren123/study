

n, m ,v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

# 그냥 곱하면 같은 차원에서 갯수가 증가한다
# for 문을 사용하면 한 차원이 증가하면서 갯수도 증가한다.


print(graph)

for i in range(m) :
    s,e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

print(graph)

# 노드의 개수 + 1 (0을 쓰고 싶지 않기 때문에 +1을 한다.)
# 지나가지 않은 것은 0, 지나온 것은 1로 표현
visited = [0] * (n+1)

# 시작 노드가 주어진다.
def dfs(node) :
    global n, graph
    visited[node] = 1
    print(node, end = ' ')
    for i in range(1, n+1) :
        if graph[node][i] == 1 and visited[i] == 0 :
            dfs(i)

# 자식을 찾으면 재귀 형식으로 계속 자식을 찾게 되는 형식이다!




