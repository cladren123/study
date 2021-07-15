import heapq
import sys


input = sys.stdin.readline

n = int(input())
m = int(input())

wire = []

for _ in range(m) :
    s,e,c = map(int, input().split())
    wire.append([c,s,e])

# for i in wire :
#     print(i)

visited = [0] * (n+1)
heapq.heapify(wire)




connect = []
allcost = 0
newheap = []
heapq.heappush(newheap, heapq.heappop(wire))

while newheap :
    cost, start, end = heapq.heappop(newheap)
    if visited[end] == 1 :
        continue
    else :
        allcost += cost
        visited[end] = 1






print(allcost)