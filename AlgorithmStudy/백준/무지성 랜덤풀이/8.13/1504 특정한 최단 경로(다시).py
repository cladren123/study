import heapq
import sys

input = sys.stdin.readline

"""
1 v1 v2 n 
1 v2 v1 n 

두 가지 경우의 수를 구해 뭐가 더 최단경로인지를 비교한다.


"""

INF = int(1e9)

n,e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e) :
    s, e, c = map(int, input().split())

    graph[s].append([c,e])
    graph[e].append([c,s])

v1, v2 = map(int, input().split())

# for i in graph :
#     print((i))

def dik(start) :
     heap = []
     heapq.heappush(heap, [0,start])

     answerlist = [INF] * (n+1)
     answerlist[start] = 0

     while heap :
         cost, cur = heapq.heappop(heap)

         if answerlist[cur] < cost :
             continue

         for ncost, nextnode in graph[cur] :
             nextcost = cost + ncost

             if nextcost < answerlist[nextnode] :
                 answerlist[nextnode] = nextcost
                 heapq.heappush(heap, [nextcost,nextnode])

     return answerlist



oridis = dik(1)
v1dis = dik(v1)
v2dis = dik(v2)


onecase = oridis[v1] + v1dis[v2] + v2dis[n]
twocase = oridis[v2] + v2dis[v1] + v1dis[n]

answer = min(onecase,twocase)

print(answer if answer < INF else -1)
