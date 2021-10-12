

import sys
from collections import deque

input = sys.stdin.readline

# n : 세로, m : 가로
n, m = map(int, input().split())

board = []

for _ in range(n) :
    one = list(map(int, input().split()))
    board.append(one)

dx = [1,0,-1,0]
dy = [0,-1,0,1]


# 치즈 가장자리 확인, 녹이기
def melt(board) :
    visited = [[0] * m for _ in range(n)]
    que = deque()
    que.append([0,0])

    visited[0][0] = 1

    while que :
        y,x = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m :
                if board[ny][nx] == 1 :
                    visited[ny][nx] += 1

                if visited[ny][nx] == 0 and board[ny][nx] == 0 :
                    visited[ny][nx] = 1
                    que.append([ny,nx])

    for i in range(n) :
        for j in range(m) :
            if visited[i][j] >= 2 :
                board[i][j] = 0


    cheezecount = 0

    for one in board :
        cheezecount += one.count(1)

    if cheezecount == 0 :
        return -1
    else :
        return 0

answer = 0

while True :
    answer += 1
    result = melt(board)

    if result == -1 :
        break



print(answer)
