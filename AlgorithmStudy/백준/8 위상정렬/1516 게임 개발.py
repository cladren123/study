import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

bt = [0] * (n+1)

# 선행순위를 알려주는 그래프, 가로로 읽으면 다음 지을 건물을 세로로 읽으면 이 건물을 짓기 위해 먼저 지어야 하는 건물들을 알 수 있다.
graph = [[0] * (n+1) for _ in range(n+1)]

# 차수를 통해 큐에 넣을지 말지 판단
ndgree = [0] * (n+1)

# 그래프를 채우는 입력단
for i in range(1,n+1) :
    ilist = list(map(int, input().split()))
    bt[i] = ilist[0]
    for j in range(1, len(ilist)) :
        if ilist[j] == -1 :
            continue
        else :
            graph[ilist[j]][i] += 1
            # graph[i][ilist[j]] += 1
            ndgree[i] += 1



que = deque()

# 차수가 0인 것에 큐에 넣는다.
for i in range(1,n+1) :
    if ndgree[i] == 0 :
        que.append(i)


# for i in graph :
#     print(i)
# print(que)

# 최종 정답이 되는 건물 짓는 시간을 이 리스트에 저장한다.
alist = [0] * (n+1)


while que :
    cur = que.popleft()

    # 건물을 짓기 위해 먼저 지어야 할 건물들 중 가장 긴 시간을 갖는 것을 찾는다.
    maxbt = 0
    for back in range(1, n+1) :
        if graph[back][cur] == 1 :
            maxbt = max(maxbt, alist[back])

    # 선행 건물 중 가장 긴 시간이 걸리는 것과 지금 지으려는 건물의 시간을 더해 정답리시트 alist에 넣는다.
    alist[cur] = bt[cur] + maxbt

    # 현재 건물을 지으면 앞으로 지을 수 있는 건물에 차수를 -1 한다. 차수가 0이 되면 que에 집어넣는다.
    for next in range(1,n+1) :
        if graph[cur][next] == 1 :
            ndgree[next] -= 1

            if ndgree[next] == 0 :
                que.append(next)

# 정답 리스트를 출력한다.
for i in range(1, n+1) :
    print(alist[i])
0



















