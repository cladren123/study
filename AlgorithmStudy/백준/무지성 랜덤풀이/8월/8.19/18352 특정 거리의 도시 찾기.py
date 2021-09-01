
"""

문제 유형 = 다익스트라 알고리즘(?) - 정답

"""
import sys
from collections import deque

input = sys.stdin.readline

# n : 도시의 개수
# m : 도로의 개수
# k : 거리 정보
# x : 출발 도시
n, m, k, x = map(int, input().split())

# 도로의 정보를 담을 리스트
graph = [[] for _ in range(n+1)]

# 도시의 방문 여부를 확인하는 리스트 0:방문안함 1:방문함
visited = [0] * (n+1)

for _ in range(m) :
    start, end = map(int, input().split())

    graph[start].append(end)

# for i in graph :
#     print(i)

que = deque()

# 출발 도시, 경로의 거리
que.append([x,0])
visited[x] = 1

answerlist = []

# 최소비용으로 적은 것을 넣어야 한다. - 다익스트라

while que :
    cur, cost = que.popleft()

    for i in graph[cur] :
        if visited[i] == 0 :
            visited[i] = 1
            newcost = cost + 1
            que.append([i,newcost])
            if newcost == k :
                answerlist.append(i)

answerlist.sort()

if len(answerlist) == 0 :
    print(-1)
else :
    for i in answerlist :
        print(i)









