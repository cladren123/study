"""

문제유형 :
그래프 이론
그래프 탐색
브루트포스 알고리즘
너비 우선 탐색

"""
import sys
from collections import deque

input = sys.stdin.readline


# n 세로 m 가로
n, m = map(int, input().split())

board = []

for _ in range(n) :
    one = input()
    one = list(one)
    board.append(one)


dx = [1,0,-1,0]
dy = [0,-1,0,1]

# L을 만날 때 마다 탐색을 해야 하나...

# 가장 긴 길을 찾는 함수
def lroad(y,x) :
    que = deque()
    visited = [[0] * m for _ in range(n)]

    que.append([y,x,0])
    visited[y][x] = 1

    answer = 0

    while que :
        y,x,count = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m :
                if visited[ny][nx] == 0 and board[ny][nx] == "L":
                    visited[ny][nx] = 1
                    newcount = count + 1
                    que.append([ny,nx,newcount])

                    answer = max(answer, newcount)

    return answer

answer = 0

for i in range(n) :
    for j in range(m) :
        if board[i][j] == "L" :
            hubo = lroad(i,j)
            answer = max(answer, hubo)

print(answer)






