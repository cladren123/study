"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색

"""

import sys
from collections import deque

input = sys.stdin.readline

# m : 가로, n : 세로,  h : 상자의 수
m,n,h = map(int, input().split())

board = [[] for _ in range(h)]


# 입력단 1:익은 토마토 0:익지 않은 토마토 -1:토마토가 없는 칸
for height in range(h) :
    for sero in range(n) :
        one = list(map(int, input().split()))
        board[height].append(one)



# 6방향 탐색 : 동남서북위아래
dx = [1,0,-1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,1,-1]

# 출력 조건
# 토마토가 익을 때까지 최소 며칠
# 토마토가 모두 익지 못하는 상황 -1
# 처음부터 모든 토마토가 익은 상태 0

que = deque();

# 방문 여부 확인 -> 중복 제거
visited = [[[0]* m for _ in range(n)] for _ in range(h)];

# 익은 토마토 탐색
for height in range(h) :
    for sero in range(n) :
        for garo in range(m) :
            if board[height][sero][garo] == 1 :
                que.append([height,sero,garo,0]);
                visited[height][sero][garo] = 1;

answer = 0
# bfs 익은 토마토의 퍼짐
while que :
    z,y,x,day = que.popleft();

    for i in range(6) :
        nz = z + dz[i];
        ny = y + dy[i];
        nx = x + dx[i];

        # 범위 체크
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m :
            # 익지 않은 토마토, 방문하지 않았으면 탐색 대상
            if board[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0 :
                board[nz][ny][nx] = 1
                visited[nz][ny][nx] = 1
                que.append([nz,ny,nx,day+1])
                answer = max(answer, day+1)

# 판 확인 : 익지 않은 토마토가 있으면 -1을 출력
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if board[i][j][k] == 0 :
                answer = -1
                break

print(answer)










