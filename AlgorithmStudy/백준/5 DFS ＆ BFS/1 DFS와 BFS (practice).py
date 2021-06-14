from collections import deque

n, m ,v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

# 그냥 곱하면 같은 차원에서 갯수가 증가한다
# for 문을 사용하면 한 차원이 증가하면서 갯수도 증가한다.

for i in range(m) :
    s,e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

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

def bfs1() :
    global n # n은 노드의 개수
    global v # v는 시작점  
    visited1 = [-1] * (n+1) # 노드를 들렀는지 확인하는 배열
    queue = deque()  # 앞에꺼 빼면 자동으로 앞으로 오는 자료형 deque
    queue.append(v) # queue 배열에 v를 넣는다.
    visited1[v] = 0 # v를 점검했으니 visited에 0을 넣어 표시한다.

    while queue : # queue 에 뭐가 있으면 계속 반복한다.
        cur = queue.popleft() # queue 배열의 맨 앞을 꺼낸다.
        print(cur, end = " ") # node 출력

        for i in range(1, n+1) : 
            # graph[cur][i] 현재 노드 cur에 연결되어있는 걸 모두 확인
            # visited[i] = -1 이면 들르지 않은 노드이다.
            if graph[cur][i] == 1 and visited1[i] == -1 :
                queue.append(i) # 조건에 충족되면 queue 배열에 집어넣는다.
                visited1[i] = visited[cur] + 1 # visited 배열에 넣는다. 몇번째 탐색자였는지


def bfs2() :
    global n
    global v

    visited2 = [0] * (n+1)

    queue = deque()
    queue.append((3,0))
    visited2[v] = 1

    while queue :
        cur = queue.popleft() # (node,depth)
        print(cur, end = " ")

        for i in range(1, n+1) :
            if graph[cur[0][i]] == 1 and visited2[i] == 0 :
                queue.append((i, cur[i] +1))
                visited2[i] = 1





dfs(v)
print()
bfs1()




