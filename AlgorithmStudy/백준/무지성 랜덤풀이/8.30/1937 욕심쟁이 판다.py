"""

문제 유형 : DFS BFS

아 나의 한계다..



"""
import sys

input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n) :
    board.append(list(map(int, input().split())))

# for i in board :
#     print(i)

visited = [[0] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dfs(y,x) :

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n :
            if board[ny][nx] > board[y][x] :
                visited[ny][nx] = max(visited[ny][nx], visited[y][x]+1 )
                dfs(ny,nx)

    return visited[y][x]


for i in range(n) :
    for j in range(n) :
        if visited[i][j] == 0 :
            visited[i][j] = 1
            dfs(i,j)


# for i in visited :
#     print(i)


answer = 0

for i in visited :
    answer = max(answer, max(i))

print(answer)




