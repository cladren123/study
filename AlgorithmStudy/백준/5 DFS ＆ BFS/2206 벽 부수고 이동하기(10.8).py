"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색


이중포문으로 벽을 탐색한 다음에 벽이 없는 경우를 만들어 대입하면
시간 초과 발생




"""

import sys
import copy
from collections import deque

input = sys.stdin.readline

# n : 세로, m : 가로
n,m = map(int, input().split());

board = []

# 0은 통로 1은 벽
# 입력단. string으로 입력해야 0을 살릴 수 있다.
for _ in range(n) :
    # sys를 사용해 스트링을 입력받으면 뒤에 공백이 생기므로 strip로 제거해준다.
    one = input().strip()
    one = list(one)
    board.append(one)

# 방향탐색 : 시계방향
dx = [1,0,-1,0]
dy = [0,-1,0,1]



def bfs() :
    # 벽 파괴 여부
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    que = deque()

    que.append([0, 0, 1])
    visited[0][0][1] = 1

    while que :
        y,x,c = que.popleft()

        if y == n-1 and x == m-1 :
            return visited[y][x][c]

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m :
                if board[ny][nx] == '1' and c == 1 :
                    visited[ny][nx][0] = visited[y][x][c] + 1
                    que.append([ny,nx,0])
                if board[ny][nx] == '0' and visited[ny][nx][c] == 0 :
                    visited[ny][nx][c] = visited[y][x][c] + 1
                    que.append([ny,nx,c])

    return -1

print(bfs())























