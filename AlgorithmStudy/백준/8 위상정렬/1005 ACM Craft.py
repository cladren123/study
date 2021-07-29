import sys
from collections import deque

input = sys.stdin.readline

# n 건물의 개수, k 건설순서규칙
n, k = map(int, input().split())

nlist = [[]  for _ in range(n+1)]


ntime = list(map(int, input().split()))
ntime.insert(0,0)

visited = [0] * (n+1)

for _ in range(k) :
    s, e = map(int, input().split())
    nlist[e].append(s)

w = int(input())

print(nlist)
print(ntime)

bt = ntime[w]
que = deque()
que.append([w, bt])


answer = 0

while que :
    print(que)
    nowb, bt = que.popleft()
    print(nowb, bt)


    if nlist[nowb] == [] :
        answer = max(answer,bt)
    else :
        answer = bt


    newbt = 0
    for i in nlist[nowb] :
        if visited[i] == 1 :
            continue
        else :
            newbt = max(newbt, ntime[i])

    check = ntime.index(newbt)
    visited[check] = 1

    bt += newbt

    for i in nlist[nowb] :
        que.append([i, bt])





print(answer)





















