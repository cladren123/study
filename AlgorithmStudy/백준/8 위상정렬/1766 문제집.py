import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

nl = [[] for _ in range(n+1)]
nd = [0] * (n+1)

for _ in range(m) :
    s,e = map(int, input().split())
    nl[s].append(e)
    nd[e] += 1

# print(nl)
# print(nd)

que = []

for i in range(1, n+1) :
    if nd[i] == 0 :
        que.append(i)

while que :
    que.sort()
    cur = que.pop(0)
    print(cur, end = " ")
    for i in nl[cur] :
        next = i
        nd[i] -= 1
        if nd[i] == 0 :
            que.append(i)








