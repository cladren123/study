

"""

세로 12줄, 가로 6줄

4개 연결되면 삭제

색깔은 5개
R G B P Y

"""

import sys
from collections import deque

input = sys.stdin.readline

board = []

for _ in range(12) :
    one = input().strip()
    one = list(one)
    board.append(one)




# 폭발하면 flag = 1, flag = 1 이면 반복
# 폭발 후 내려오는 모듈 작성
# 땅바닥은 board[11][*]

# 4방향 탐색
dx = [1,0,-1,0]
dy = [0,-1,0,1]

answer = 0

# 상하좌우로 4개 있으면 폭발
def bombmodul() :
    global answer
    que = deque()
    visited = [[0] * 6 for _ in range(12)]
    flag = 0
    bomblist = []

    for y in range(12) :
        for x in range(6) :
            if board[y][x] != "." and visited[y][x] == 0 :
                que.append([y,x,board[y][x]])
                visited[y][x] = 1
                bomb = []
                bomb.append([y,x])

                while que :
                    y,x,color = que.popleft()

                    for i in range(4) :
                        ny = y + dy[i]
                        nx = x + dx[i]

                        if 0 <= ny < 12 and 0 <= nx < 6 :
                            if board[ny][nx] == color and visited[ny][nx] == 0 :
                                que.append([ny,nx,color])
                                visited[ny][nx] = 1
                                bomb.append([ny,nx])
                # 4개가 연결되어 있으면 bomb리스트에 넣는다.
                if len(bomb) >= 4 :
                    bomblist = bomblist + bomb

    if len(bomblist) >= 1 :
        flag = 1
        answer += 1

    # 폭파시키고 내리는 작업을 하자.
    bomblist.sort()


    downlist = []
    down = [0] * 6
    # 폭파
    for y,x in bomblist :
        if board[y-1][x] != "." :
            downlist.append(x)
        board[y][x] = "."
        down[x] += 1

    # 내려오는 함수
    stack = [[] for _ in range(6)]
    for i in downlist :
        for j in range(11,-1,-1) :
            if board[j][i] != "." :
                stack[i].append(board[j][i])
                board[j][i] = "."

    for i in downlist :
        count = 0
        for j in range(11,11-len(stack[i]), -1) :
            board[j][i] = stack[i][count]
            count += 1

    # for i in board :
    #     print(i)
    # print()



    return flag

flag = 1
while flag :
    flag = bombmodul()

print(answer)















