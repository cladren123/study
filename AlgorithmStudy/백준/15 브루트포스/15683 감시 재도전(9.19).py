"""

cctv
1 : 4
2 : 2
3 : 4
4 : 4
5 : 1

0 1 2 3


"""
import copy
import sys
from collections import deque

input = sys.stdin.readline

# n : 세로, m : 가로
n,m = map(int, input().split())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

# 동, 남, 서, 북 시계방향으로 돈다
dx = [1,0,-1,0]
dy = [0,-1,0,1]

cctvtype = [1,2,3,4,5]

ctype4 = [1,3,4]
ctype2 = [2]
ctype1 = [5]

cctv = []

for i in range(n) :
    for j in range(m) :
        # cctv를 [y,x,시작방향]으로 담는다.
        # 방향으로 dfs를 돌거기 때문에
        if board[i][j] in cctvtype :
            cctv.append([i,j,0,board[i][j]])

cctvcount = len(cctv)

def watch(board, y, x, direct) :
    que = deque()
    que.append([y,x])

    while que :
        y,x = que.popleft()

        ny = y + dy[direct]
        nx = x + dx[direct]

        if 0 <= ny < n and 0 <= nx < m :
            if board[ny][nx] == 6 :
                return
            else :
                board[ny][nx] = "#"
                que.append([ny,nx])

def countboard(board) :
    zcount = 0
    for i in board :
        zcount += i.count(0)

    return zcount

def solve(stage) :
    # 종단조건
    global board, answer
    if stage == cctvcount :
        subboard = copy.deepcopy(board)

        for y,x,direct,ctype in cctv :
            if ctype == 1 :
                watch(subboard, y, x, direct)
            elif ctype == 2 :
                watch(subboard, y, x, direct)
                watch(subboard, y, x, (direct+2)%4)
            elif ctype == 3 :
                watch(subboard, y, x, direct)
                watch(subboard, y, x, (direct+1)%4)
            elif ctype == 4 :
                watch(subboard, y, x, direct)
                watch(subboard, y, x, (direct+1)%4)
                watch(subboard, y, x, (direct+2)%4)
            elif ctype == 5 :
                watch(subboard, y, x, direct)
                watch(subboard, y, x, direct+1)
                watch(subboard, y, x, direct+2)
                watch(subboard, y, x, direct+3)

        answer = min(answer, countboard(subboard))

        return

    # 경우의 수를 구하는 부분
    if board[cctv[stage][0]][cctv[stage][1]] in ctype4 :
        for i in range(4) :
            # cctv의 방향을 바꿔가면서 다음 것을 탐색한다.
            cctv[stage][2] = i
            solve(stage+1)
    elif board[cctv[stage][0]][cctv[stage][1]] in ctype2 :
        for i in range(2) :
            cctv[stage][2] = i
            solve(stage+1)
    else :
        solve(stage+1)

answer = sys.maxsize
solve(0)

print(answer)





