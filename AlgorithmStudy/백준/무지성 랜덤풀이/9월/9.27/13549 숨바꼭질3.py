"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색
다익스트라
0-1 너비 우선 탐색

시간초과 발생
범위를 지정해서 범위가 초과하는 것들을 걷어내니 해결할 수 있었다.

"""
import sys
from collections import deque

input = sys.stdin.readline

# n : 수빈 k : 동생
n, m = map(int, input().split())



maxnum = 100001

visited = [0] * maxnum
timelist = [-1] * maxnum

# 초기화 하는 과정도 중요하다.
que = deque()
que.append(n)
timelist[n] = 0
visited[n] = 1

while que :
    loc = que.popleft()
    # *2 인 경우
    if loc*2 < maxnum and visited[loc*2] == 0 :
        timelist[loc*2] = timelist[loc]
        visited[loc*2] = 1
        que.appendleft(loc*2)

    # +1 인 경우
    if loc+1 < maxnum and visited[loc+1] == 0 :
        visited[loc+1] = 1
        timelist[loc+1] = timelist[loc] + 1
        que.append(loc+1)

    # -1 인 경우
    if loc-1 >= 0 and visited[loc-1] == 0 :
        visited[loc-1] = 1
        timelist[loc-1] = timelist[loc] + 1
        que.append(loc-1)

print(timelist[m])



















