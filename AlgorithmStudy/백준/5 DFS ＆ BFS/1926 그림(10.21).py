"""

파이썬 통과
pypy3 메모리 초과

"""

import sys

sys.setrecursionlimit(10000000)

input = sys.stdin.readline

# n : 세로, m : 가로
n, m = map(int, input().split())

# 그림 입력
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

# 4방향 탐색
dx = [1,0,-1,0]
dy = [0,-1,0,1]

visited = [[0] * m for _ in range(n)]


def dfs(y,x) :
    global board;
    global count
    visited[y][x] = 1
    count += 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m :
            if board[ny][nx] == 1 and visited[ny][nx] == 0 :
                visited[ny][nx] = 1
                dfs(ny,nx)

alist = []

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 and visited[i][j] == 0 :
            count = 0
            dfs(i,j)
            alist.append(count)

answer1 = len(alist)


if answer1 == 0 :
    print(0)
    print(0)
else :
    print(answer1)
    print(max(alist))