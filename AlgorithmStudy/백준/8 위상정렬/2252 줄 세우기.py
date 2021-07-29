import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

nlist = [[] for _ in range(n+1)]
ndegree = [0] * (n+1)

for _ in range(m) :
    s,e = map(int, input().split())
    nlist[s].append(e)
    ndegree[e] += 1

# print(nlist)
# print(ndegree)

que = deque()

for i in range(1, n+1) :
    if ndegree[i] == 0 :
        que.append(i)



while que :
    cur = que.popleft()

    print(cur, end = " ")

    for i in nlist[cur] :
        check = i
        ndegree[check] -= 1
        if ndegree[check] == 0 :
            que.append(check)







