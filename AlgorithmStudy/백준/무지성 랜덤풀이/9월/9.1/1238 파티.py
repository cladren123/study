
"""

문제 유형 : 다익스트라

"""
import heapq
import sys

input = sys.stdin.readline


n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,e,cost = map(int, input().split())
    graph[s].append([e, cost])


def dik(start, end) :
    answerlist = [sys.maxsize] * (n + 1)
    heap = []
    heapq.heappush(heap, [0, start])
    answerlist[start] = 0

    while heap :
        cost, cur = heapq.heappop(heap)

        if answerlist[cur] < cost :
            continue

        for nextnode, ncost in graph[cur] :
            nextcost = cost + ncost

            if nextcost < answerlist[nextnode] :
                answerlist[nextnode] = nextcost
                heapq.heappush(heap, (nextcost, nextnode))

    answer = answerlist[end]

    return answer

ans = [0] * (n+1)

for i in range(1,n+1) :
    ans[i] = dik(i,x) + dik(x,i)

# print(ans)
print(max(ans))


















