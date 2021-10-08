"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색
플로이드-와샬

"""

import sys
from collections import deque

que = deque()

# n : 유저의 수, m : 친구 관계의 수
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 케빈-베이컨 수 구하기
def bfs(node) :
    que = deque()
    que.append(node)

    visited = [0] * (n+1)

    while que :
        now = que.popleft()

        for nextnode in graph[now] :
            if visited[nextnode] == 0 :
                visited[nextnode] = visited[now] + 1
                que.append(nextnode)

    return sum(visited)


alist = [0] * (n+1)
answernum = sys.maxsize

for i in range(1,n+1) :
    alist[i] = bfs(i)
    answernum = min(answernum, alist[i])


for i in range(1,n+1) :
    if alist[i] == answernum :
        print(i)
        break