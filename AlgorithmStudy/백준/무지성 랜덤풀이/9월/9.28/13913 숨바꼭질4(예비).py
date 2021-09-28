"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색

40% 시간초과

"""
import sys
from collections import deque

input = sys.stdin.readline

# n : 수빈, k : 동생
n, k = map(int, input().split())

maxnum = 100001

# pypy3 메모리초과, python 초과가
timelist = [-1] * maxnum
visited = [0] * maxnum

que = deque()
que.append([n,[n]])
timelist[n] = 0
visited[n] = 1

flag = 0

while que :
    now, route = que.popleft()

    n1 = now+1
    n2 = now-1
    n3 = now*2

    for nextnode in [n1,n2,n3] :
        if nextnode == k :
            time = timelist[now] + 1
            print(time)
            route = route+[nextnode]
            print(*route)
            flag = 1
            break

    if flag :
        break

    if n3 < maxnum and visited[n3] == 0:
        visited[n3] = 1
        timelist[n3] = timelist[now] + 1
        que.append([n3, route + [n3]])

    if n1 < maxnum and visited[n1] == 0 :
        visited[n1] = 1
        timelist[n1] = timelist[now] + 1
        que.append([n1, route + [n1]])

    if n2 >= 0 and visited[n2] == 0 :
        visited[n2] = 1
        timelist[n2] = timelist[now] + 1
        que.append([n2, route + [n2]])
















