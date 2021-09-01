"""
이분탐색, BFS 문제

"""



import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

s = [[] for _ in range(n+1)]

for _ in range(m) :
    n1, n2, cost = map(int, input().split())

    s[n1].append([n2,cost])
    s[n2].append([n1,cost])

# for i in s :
#     print(i)

start, end = map(int, input().split())

def bfs(mid) :
    visited[start] = 1
    que = deque()
    que.append(start)

    while que :
        newstart = que.popleft()
        if newstart == end :
            return True

        for nextn, nextcost in s[newstart] :
            if visited[nextn] == 0 and mid <= nextcost :
                que.append(nextn)
                visited[nextn] = 1

    return False



left, right = 1, 1000000000

while left <= right :
    visited = [0] * (n+1)
    mid = (left + right) // 2
    if bfs(mid) :
        left = mid + 1
    else :
        right = mid - 1

print(right)








