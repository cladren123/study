import copy
import sys
from collections import deque


input = sys.stdin.readline

# 양방향 가능
# 이분탐색이었다
# 시간 초과 났다. ㅠㅠ

n,m = map(int, input().split())

nl = []

for _ in range(m) :
    one = list(map(int, input().split()))
    nl.append(one)

start, end = map(int, input().split())

que = deque()



for i in nl :
    visited = []
    visited.append(start)

    if i[0] == start :
        visited.append(i[1])
        que.append([i[2], visited])
    elif i[1] == start :
        visited.append(i[0])
        que.append([i[2], visited])



answer = 0

while que :
    one = que.popleft()
    cost = one[0]
    newvisited1 = copy.deepcopy(one[1])
    newvisited2 = copy.deepcopy(one[1])

    if end in one[1] :
        answer = max(answer, cost)

    for i in range(m) :
        if nl[i][0] in one[1] and nl[i][1] not in one[1] :
            newvisited1.append(nl[i][1])
            newcost = min(cost, nl[i][2])
            que.append([newcost, newvisited1])

        if nl[i][0] not in one[1] and nl[i][1] in one[1] :
            newvisited2.append(nl[i][0])
            newcost = min(cost, nl[i][2])
            que.append([newcost, newvisited2])


print(answer)



































