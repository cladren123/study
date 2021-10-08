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
    # 방문여부와 벽 파괴 여부를 저장
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    que = deque()

    # 1은 벽을 파괴할 기회가 있다.
    que.append([0, 0, 1])
    visited[0][0][1] = 1

    # 탐색 시작
    while que :
        y,x,c = que.popleft()

        # 목적지에 도착하면 몇 칸 걸렸는지를 리턴한다.
        if y == n-1 and x == m-1 :
            return visited[y][x][c]

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위를 벗어나지 않았을 때 탐색
            if 0 <= ny < n and 0 <= nx < m :
                # 벽을 만날 경우 기회를 사용하고(c가 1에서 0이 된다.) 계속 탐색
                if board[ny][nx] == '1' and c == 1 :
                    visited[ny][nx][0] = visited[y][x][c] + 1
                    que.append([ny,nx,0])
                # 벽이 없는 경우 평범히 탐색
                if board[ny][nx] == '0' and visited[ny][nx][c] == 0 :
                    visited[ny][nx][c] = visited[y][x][c] + 1
                    que.append([ny,nx,c])

    # 목적지에 도착하지 못하면 -1을 리턴 
    return -1

print(bfs())























