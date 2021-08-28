"""

문제 유형 : DFS BFS

경로 탐색 문제에서 목적지까지 갈 수 있는 경로의 개수를 구해야 한다.
경로의 개수를 구할 경우 잘 터지기 때문에 dp를 사용한다.

BFS로 풀어보려 했지만.. 경로가 곂치면  이 경로가 결승점까지 닿을지 안닿을지 모르기 때문에 사용할 수 가 없다.

결국 DFS를 사용해 정답에 도달하는 길을 찾고 그 경로와 곂처지면 +1 을 하고 탐색을 멈춰서 시간을 줄이는 방법을 써야 한다.


"""
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

board = []

for _ in range(m) :
    board.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(m)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

que = deque()

que.append([0,0,board[0][0]])

answer = 0

while que :
    y, x, cur = que.popleft()


    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < m and 0 <= nx < n :
            if cur > board[ny][nx] :
                if visited[ny][nx] == 0 :
                    que.append([ny,nx,board[ny][nx]])
                    visited[ny][nx] = 1

                    if ny == m-1 and nx == n-1 :
                        answer += 1

                elif visited[ny][nx]

print(answer)




