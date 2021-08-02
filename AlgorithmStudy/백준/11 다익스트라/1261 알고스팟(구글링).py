
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
a = []

for i in range(m):
    a.append(sys.stdin.readline())

dist = [[-1 ] *n for _ in range(m)]
dist[0][0] = 0
q = deque()
dx = [1 ,-1 ,0 ,0]
dy = [0 ,0 ,1 ,-1]
q.append([0, 0])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+ dx[i], y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if dist[nx][ny] == -1:
                if a[nx][ny] == '0':
                    # 먼저 왼쪽에 넣음, 벽이 아니니까 +=1 을 하지 않는다.
                    q.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                elif a[nx][ny] == '1':
                    q.append([nx, ny])
                    # 벽을 만났으니까 += 1 을 한다.
                    dist[nx][ny] = dist[x][y] + 1

print(dist[m - 1][n - 1])