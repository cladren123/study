"""
너비 우선 탐색 BFS

"""
import sys
from collections import deque

input = sys.stdin.readline

# 정점, 간선 개수 입력
n, m = map(int, input().split())

# 방문 여부를 나타내는 리스트
visited = [0] * (n+1)

# 간선에 연결 정보를 담을 리스트
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s, e = map(int, input().split())

    # 양방향 연결이므로 양쪽에 다 넣어준다.
    graph[s].append(e)
    graph[e].append(s)

# 연결 요소의 개수를 세는 변수
count = 0

# 연결 요소를 찾는 함수
def bfs(start) :
    global count

    # 같이 연결되었으면 visited에 같은 숫자로 기록된다.
    count += 1

    # start 부터 탐색하게 된다.
    visited[start] = count

    que = deque()
    que.append(start)

    # 연결되어 있는 노드들을 탐색하낟.
    while que :
        cur = que.popleft()

        # 현재 노드와 연결되어 있는 노드들을 확인
        for i in graph[cur] :

            # 방문하지 않았다면 연결카운트를 부여하고 que에 넣어서 계속해서 탐색한다.
            if visited[i] == 0 :
                visited[i] = count
                que.append(i)

    # 더 이상 방문할 데가 없으면 while 문은 끝난다.


# visited 함수를 통해 방문하지 않은 요소를 bfs에 돌린다.
for i in range(1,n+1) :
    if visited[i] == 0 :
        bfs(i)

# 답 출력
print(count)







