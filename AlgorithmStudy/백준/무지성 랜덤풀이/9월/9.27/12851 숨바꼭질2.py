"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색

"""
import sys
from collections import deque

input = sys.stdin.readline

maxnum = 100001

# n : 수빈 k : 동생
n, k = map(int, input().split())

# 이미 도착해 있으면 2번째 부분 +1
timelist = [[-1,0] for _ in range(maxnum)]
visited = [0] * maxnum

que = deque()
que.append(n)
visited[n] = 1
timelist[n][0] = 0
timelist[n][1] = 1


while que :
    now = que.popleft()

    n1 = now + 1
    n2 = now - 1
    n3 = now * 2

    if n3 < maxnum :
        if visited[n3] == 0 :
            visited[n3] = 1
            timelist[n3][0] = timelist[now][0] + 1
            timelist[n3][1] += 1
            que.append(n3)
        elif visited[n3] == 1 :
            if timelist[n3][0] == timelist[now][0] + 1 :
                timelist[n3][1] +=1
                que.append(n3)

    if n1 < maxnum :
        if visited[n1] == 0 :
            visited[n1] = 1
            timelist[n1][0] = timelist[now][0] + 1
            timelist[n1][1] += 1
            que.append(n1)
        elif visited[n1] == 1 :
            if timelist[n1][0] == timelist[now][0] + 1 :
                timelist[n1][1] +=1
                que.append(n1)

    if n2 >= 0 :
        if visited[n2] == 0 :
            visited[n2] = 1
            timelist[n2][0] = timelist[now][0] + 1
            timelist[n2][1] += 1
            que.append(n2)
        elif visited[n2] == 1 :
            if timelist[n2][0] == timelist[now][0] + 1 :
                timelist[n2][1] +=1
                que.append(n2)


print(timelist[k][0])
print(timelist[k][1])







