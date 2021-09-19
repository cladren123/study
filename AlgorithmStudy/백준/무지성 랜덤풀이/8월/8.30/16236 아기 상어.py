
"""

문제 유형 : 구형

위 왼을 먼저 먹는다

자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
크기 2인 아기상어, 물고기 2마리 먹으면 크기 3

몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있을까

0 : 빈칸
1,2,3,4,5,6 : 물고기 크기
9.19 : 아기상어 위치

처음 아기상어의 크기는 2 이다.

큰 물고기는 지나갈 수가 없데... BFS로 풀어야한다.

"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n) :
    board.append(list(map(int, input().split())))

baby = 2

sharky = 0
sharkx = 0

# 아기 상어 좌표값 찾기
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 9 :
            sharky = i
            sharkx = j

board[sharky][sharkx] = 0

# 성장하기 위해 얼마나 먹었는지 체크
count = 0
answer = 0

dx = [1,0,-1,0]
dy = [0,-1,0,1]

que = deque()
que.append([sharky,sharkx,0])

mint = 1

while mint :
    hubo = []
    visited = [[0] * n for _ in range(n)]

    if count == baby :
        baby += 1
        count = 0

    while que :
        y,x,guri = que.popleft()

        visited[y][x] = 1

        guricheck = 10000

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n :
                if 0 < board[ny][nx] < baby and visited[ny][nx] == 0 :
                    if guricheck >= guri + 1 :
                        guricheck = guri + 1
                        hubo.append([ny,nx,guricheck])

                if baby >= board[ny][nx] and visited[ny][nx] == 0 :
                    newguri = guri + 1
                    que.append([ny,nx,newguri])
                    visited[ny][nx] = 1

    if len(hubo) == 0 :
        mint = 0

    else :
        hubo.sort(key=lambda x:(x[2], x[0], x[1]))

        newy = hubo[0][0]
        newx = hubo[0][1]

        answer += hubo[0][2]
        que.append([newy,newx,0])

        board[newy][newx] = 0
        count += 1


print(answer)















