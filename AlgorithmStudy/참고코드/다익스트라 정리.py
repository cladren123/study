
"""
다익스트라 알고리즘
비용이 적게 드는 최단 경로를 구하는 알고리즘

예시 : 1753 최단경로

첫째 줄에 정점의 개수 v, 간선의 개수 e
둘째 줄에는 시작 정점의 번호 k
셋째 줄부터 e개의 줄의 걸처 간선이 주어진다.
간선은 3개의 정수 (u,v,w)가 순서대로 주어진다. => u에서 v로 가는 가중치 w

서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있다.

방향그래프가 주어진다.
주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구할 때 쓰는게 다익스트라 알고리즘이다.

graph 라는 이중 리스트를 만들어 간선이 정보를 담는다.
graph[1] 에는 1 노드에서 갈 수 있는 노드와 비용의 정보가 담기게 된다.

u,v 로 가는 간선 중 최소값을 뽑을 heap 을 생성한다.
heap은 최소값이 맨 앞으로 온다. (비용이 최소값인 것을 뽑을 수 있다.)

이 heap을 이용해 while 문을 돌린다.
heappop을 통해 heap에 담겨 있는 정보를 토대로 다음 노드로 이어질 것을 찾는다.

이 때 연결된 가중치는 costlist에 담는다.
costlist에 담을 때 기존에 담겨있는 것과 비교해서 더 적은 값을 담는다.




"""
import heapq
import sys

input = sys.stdin.readline

v,e = map(int, input().split())

k = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e) :
    start,end,cost = map(int, input().split())

    graph[start].append([cost,end])

heap = []
heapq.heappush(heap, [0,k])

costlist = [sys.maxsize] * (v+1)

while heap :
    cost, cur = heapq.heappop(heap)


    if costlist[cur] > cost :
        costlist[cur] = cost

    for ncost, nextnode in graph[cur] :
        nextcost = cost + ncost

        if nextcost < costlist[nextnode] :
            heapq.heappush(heap, [nextcost, nextnode])


for i in range(1, v+1) :
    if costlist[i] == sys.maxsize :
        print("INF")
    else :
        print(costlist[i])












