
"""
실버1


"""

# m:가로칸 n:세로칸
from collections import deque

m,n = map(int, input().split())

# 1:은 익은 토마토 0:익지 않은 토마토 -1:토마토가 들어있지 않은 칸
board = [list(map(int, input().split())) for _ in range(n)]

visited= [[-3] * m for _ in range(n)]



que = deque()

dx = [1,0,-1,0]
dy = [0,-1,0,1]

count = 0

for i in range(n) :
    for j in range(m) :
        if board[i][j] == -1 :
            visited[i][j] = -1

        if board[i][j] == 1 :
            que.append([i,j])
            visited[i][j] = count

while que :
    y,x = que.popleft()

    for i in range(4) :
        nexty = y + dy[i]
        nextx = x + dx[i]

        if 0 <= nexty < n and 0 <= nextx < m :
            if board[nexty][nextx] == 0 and visited[nexty][nextx] == -3 :
                que.append([nexty,nextx])
                visited[nexty][nextx] = visited[y][x] + 1
                board[nexty][nextx] = 1

answer = 0
for i in visited :
    if -3 in i :
        answer = -1
        break
    else :
        if answer < max(i) :
            answer = max(i)

print(answer)


# for i in board :
#     print(i)
#
# print()
#
# for i in visited :
#     print(i)










