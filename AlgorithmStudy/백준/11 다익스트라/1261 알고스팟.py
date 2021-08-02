import heapq
import sys

input = sys.stdin.readline


# m은 가로, n은 세로
m, n = map(int, input().split())


graph = ['0' * (m+1)]

for _ in range(n) :
    one = "0" + input().strip()
    graph.append(one)

for i in graph :
    print(i)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

heap = []
heapq.heappush(heap, [0, 0, 0])

print(heap)

while heap :
















