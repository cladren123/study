"""

문제유형 :
구현
그래프 이론
그래프 탐색
너비 우선 탐색
시뮬레이션

"""
import copy
import sys
from collections import deque

input = sys.stdin.readline

# n : 땅의 크기, l : 인구 차이 최소, r : 인구 차이 최대
n, l, r = map(int, input().split())

board = []

for _ in range(n) :
    one = list(map(int, input().split()))
    board.append(one)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def bfs(i,j,visited,board) :
    que = deque()
    que.append([i,j])
    visited[i][j] = 1

    group = []
    group.append([i,j])
    result = board[i][j]
    count = 1


    while que :
        y,x = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 :
                if l <= abs(board[y][x] - board[ny][nx]) <= r :
                    visited[ny][nx] = 1
                    que.append([ny,nx])
                    group.append([ny,nx])
                    result += board[ny][nx]
                    count += 1

    if count != 0 :
        ingu = result // count
        for y,x in group :
            board[y][x] = ingu

def movement() :
    global board

    visited = [[0] * n for _ in range(n)]

    que = deque()

    newboard = copy.deepcopy(board)

    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 :
                bfs(i,j,visited,board)


    if newboard == board :
        return -1
    else :
        return 1

answer = 0
flag = 1

while flag :
    flag = movement()
    if flag == -1 :
        break

    answer += 1

print(answer)




