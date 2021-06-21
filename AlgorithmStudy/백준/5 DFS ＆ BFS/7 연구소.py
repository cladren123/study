# 골드5

# n 세로 m 가로
import copy
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]


# 0 빈 칸, 1 벽, 2 바이러스
# 벽을 세우고 바이러스를 돌리자.

dx = [1,0,-1,0]
dy = [0,-1,0,1]
answer = 0



# 벽 세우기
# 여기를 바꾸니까 시간 초과가 해결되었다.
def wall(start, count) :
    if count == 3 :
        bfs()
        return
    else :
        for i in range(start, n*m) :
            r = i // m
            c = i % m
            if board[r][c] == 0 :
                board[r][c] = 1
                wall(i, count + 1)
                board[r][c] = 0

# 안전구역 확인하기
def bfs() :
    global answer
    que = deque()
    board2 = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                que.append([i, j])

    while que :
        y,x = que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n :
                if board2[ny][nx] == 0 :
                    board2[ny][nx] = 2
                    que.append([ny,nx])
    count = 0
    for i in board2 :
        count += i.count(0)
    answer = max(answer, count)
    return

wall(0,0)
print(answer)



