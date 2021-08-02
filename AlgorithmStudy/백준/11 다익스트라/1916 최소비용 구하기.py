


import copy
import heapq
import sys
from collections import deque

input = sys.stdin.readline


# n : 도시의 개수
n = int(input())

# m : 버스의 개수
m = int(input())

# 이 버스를 타면 어디로 갈 수 있는지와 비용을 담을 리스트 생성
graph = [[] for _ in range(n+1)]


for _ in range(m) :
    s, e, c = map(int,input().split())
    graph[s].append([e,c])

start, end = map(int, input().split())

# print(graph)

que = []
heapq.heappush(que, [start, 0])

# print(que)

alist = [100001] * (n+1)

while que :
    one = heapq.heappop(que)
    # print(one)
    cur = one[0]
    cost = one[1]


    if alist[cur] > cost :
        alist[cur] = cost

    for i in range(len(graph[cur])) :
        newcost = 0
        newcost = graph[cur][i][1] + cost

        if alist[graph[cur][i][0]] > newcost :
            alist[graph[cur][i][0]] = newcost
            que.append([graph[cur][i][0], newcost])


# print(alist)
print(alist[end])












