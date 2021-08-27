"""

문제 유형 : BFS, DFS

"""
import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

board = [[1] * n for _ in range(m)]

sq = []

for _ in range(k) :
    sq.append(list(map(int, input().split())))

for i in sq :
    x1, y1, x2, y2 = i

    for j in range(x1,x2) :
        for k in range(y1,y2) :
            board[k][j] = 0

answer = []

que = deque()

visited = [[0] * n for _ in range(m)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]



for i in range(m) :
    for j in range(n) :

        if board[i][j] == 1 and visited[i][j] == 0 :
            count = 1
            que.append([i,j])
            visited[i][j] = 1


            while que :
                y, x = que.popleft()

                for k in range(4) :
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < m and 0 <= nx < n :
                        if visited[ny][nx] == 0 and board[ny][nx] == 1 :
                            que.append([ny,nx])
                            visited[ny][nx] = 1
                            count += 1

            answer.append(count)

answer.sort()

print(len(answer))
print(*answer)












