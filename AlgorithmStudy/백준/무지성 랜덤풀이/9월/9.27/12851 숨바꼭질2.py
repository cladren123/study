"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색

"""
import sys
from collections import deque

input = sys.stdin.readline

# 범위의 최대값
maxnum = 100001

# n : 수빈 k : 동생
n, k = map(int, input().split())

# x 지점에 도착했을 때의 시간, 방법의 수를 저장
timelist = [[-1,0] for _ in range(maxnum)]

# x 지점에 도착했는지 여부를 표시
visited = [0] * maxnum

# 시작점에 que에 넣고 리스트들에 표현한다.
# timelist, visited에 넣지 않으면 78%에서 오답이 나온다
# 수빈이와 동생의 위치가 같을 때 답이 1이 나와야 하기 때문이다.
que = deque()
que.append(n)
visited[n] = 1
timelist[n][0] = 0
timelist[n][1] = 1

# 범위에 맞게 탐색 시작
# 이미 방문해 visited[x] = 1 이면 timelist[x][1]만 +1을 한다.
while que :
    now = que.popleft()

    n1 = now + 1
    n2 = now - 1
    n3 = now * 2

    # n*2 인 경우
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

    # n+1 한 경우
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

    # n-1 한 경우
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

# 정답 출력
print(timelist[k][0])
print(timelist[k][1])







