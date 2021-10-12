
import sys
from collections import deque

input = sys.stdin.readline


n, k = map(int, input().split())
que = deque()

for i in range(1,n+1) :
    que.append(i)

alist = []
count = 0

while que :
    now = que.popleft()

    count += 1

    if count == k :
        alist.append(now)
        count = 0
    else :
        que.append(now)



print("<", end="")

for i in range(n-1) :
    print(alist[i], end = ", ")

print(alist[n-1],end=">")









