from collections import deque

import sys


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

# for i in board :
#     print(i)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

que = deque()
que.append([0,0])

while que :
    y, x = que.popleft()

    if dp[y][x] == -1 :
        continue

    for i in range(4) :
        nexty = y + dy[i]
        nextx = x + dx[i]
        if 0 <= nexty <= n-1 and 0 <= nextx <= m-1 :
            if board[y][x] > board[nexty][nextx] :
                que.append([nexty, nextx])
                dp[nexty][nextx] += 1


print(dp[n-1][m-1])



