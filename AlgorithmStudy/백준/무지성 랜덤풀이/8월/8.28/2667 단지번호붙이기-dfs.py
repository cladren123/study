
"""

문제 유형 : BFS, DFS

DFS로 다시 풀어보기

"""
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n) :
    board.append(input())


visited = [[0] * n for _ in range(n)]

answer = []

count = 0

def dfs(y,x) :
    global count

    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n :
            if board[ny][nx] == '1' and visited[ny][nx] == 0 :
                visited[ny][nx] = 1
                count += 1
                dfs(ny,nx)



for i in range(n) :
    for j in range(n) :
        if board[i][j] == '1' and visited[i][j] == 0 :
            visited[i][j] = 1
            count = 1
            dfs(i,j)
            answer.append(count)



print(len(answer))
answer.sort()
for i in answer :
    print(i)


