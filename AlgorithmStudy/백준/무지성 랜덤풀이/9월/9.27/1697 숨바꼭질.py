"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색

"""
import sys
from collections import deque

input = sys.stdin.readline

# n : 수빈, k : 동생
n, k = map(int, input().split())

# 최대값 설정하는 변수
maxnum = 100001

# 도달하는 시간을 저장한 리스트
timelist = [-1] * maxnum

# 해당 지점을 방문했는지 표시하는 리스트
visited = [0] * maxnum

# bfs를 돌린 deque 생성
que = deque()
que.append(n)
timelist[n] = 0
visited[n] = 1

while que :
    now = que.popleft()

    n1 = now+1
    n2 = now-1
    n3 = now*2

    # 경우의 수에 맞게 범위에 맞는 탐색 시작
    if n1 < maxnum and visited[n1] == 0 :
        visited[n1] = 1
        timelist[n1] = timelist[now] + 1
        que.append(n1)

    if n2 >= 0 and visited[n2] == 0 :
        visited[n2] = 1
        timelist[n2] = timelist[now] + 1
        que.append(n2)

    if n3 < maxnum and visited[n3] == 0 :
        visited[n3] = 1
        timelist[n3] = timelist[now] + 1
        que.append(n3)

# 정답출력
print(timelist[k])