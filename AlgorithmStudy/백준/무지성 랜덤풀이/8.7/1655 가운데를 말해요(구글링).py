import heapq
import sys

input = sys.stdin.readline

n = int(input())

smallheap = []
bigheap = [int(input())]

print(bigheap[0])

for i in range(2, n+1) :
    one = int(input())

    if bigheap[0] > one :
        heapq.heappush(smallheap, -one)
    else :
        heapq.heappush(bigheap, one)


    while len(bigheap) < (i//2)+1 :
        heapq.heappush(bigheap, -heapq.heappop(smallheap))
    while len(smallheap) < i-(i//2)+1 :
        heapq.heappush(smallheap, -heapq.heappop(bigheap))

    print(bigheap[0])









