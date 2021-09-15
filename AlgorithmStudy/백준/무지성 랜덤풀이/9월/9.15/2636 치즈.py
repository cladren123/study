
"""

문제 유형 :
구현
그래프 이론
그래프 탐색
너비 우선 탐색
시뮬레이션

"""
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
board = []

for _ in range(m) :
    board.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board[0][0] = 2

def seeboard() :
    for i in board :
        print(i)
    print()

# 가장자리 공기를 2로 바꾸는 함수
def air() :
    global board
    visited1 = [[0] * n for _ in range(m)]

    que = deque()

    que.append([0,0])

    while que :
        y,x = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0 <= nx < n :
                if visited1[ny][nx] == 0 :
                    if board[ny][nx] == 0 or board[ny][nx] == 2 :
                        visited1[ny][nx] = 1
                        board[ny][nx] = 2
                        que.append([ny, nx])


def bfs(y,x,visited) :
    global board

    que = deque()
    que.append([y,x])

    while que :
        y,x = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0 <= nx < n :
                if board[ny][nx] == 2 :
                    board[y][x] = 0
                if visited[ny][nx] == 0 and board[ny][nx] == 1 :
                    visited[ny][nx] = 1
                    que.append([ny,nx])

def cheeze () :
    global board
    visited = [[0] * n for _ in range(m)]
    for i in range(m) :
        for j in range(n) :
            if board[i][j] == 1 and visited[i][j] == 0 :
                visited[i][j] = 1
                bfs(i,j,visited)
    answer = 0
    for i in board :
        answer += i.count(1)

    return answer


checker = 1
cheezecheck = 0
answer1 = 0
answer2 = 0

for i in board :
    answer2 += i.count(1)


while checker :
    answer1 += 1

    seeboard()

    air()
    seeboard()
    cheezecheck = cheeze()

    if cheezecheck == 0 :
        break

    answer2 = cheezecheck

print(answer1, answer2)







