
# 메모리초과뜸.. 시발
# 딕셔너리로 풀어야 하나...


import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

bt = [0] * (n+1)
indgree = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,8) :
    one = list(map(int,input().split()))

    bt[i] = one[0]

    for j in range(2,2+one[1]) :
        indgree[i] += 1
        graph[one[j]][i] = 1


# print(indgree)
# for i in graph :
#     print(i)

que = deque()

for i in range(1,n+1) :
    if indgree[i] == 0 :
        que.append(i)


while que :
    cur = que.popleft()

    newbt = 0
    for i in range(1,n+1) :
        if graph[i][cur] == 1 :
            newbt = max(newbt, bt[i])
    bt[cur] = bt[cur] + newbt

    for j in range(1, n+1) :
        if graph[cur][j] == 1 :
            indgree[j] -= 1

            if indgree[j] == 0 :
                que.append(j)

print(max(bt))





