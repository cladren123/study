"""

문제 유형 : DFS BFS


"""
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

visited = [[-1] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dfs(y,x) :
    if visited[y][x] < 0 :
        visited[y][x] = 0

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n :
                if board[y][x] < board[ny][nx] :
                    visited[y][x] = max(visited[y][x], dfs(ny,nx))
        visited[y][x] += 1
    return visited[y][x]


answer = 0


for i in range(n) :
    for j in range(n) :
        answer = max(answer, dfs(i,j))

print(answer)

# for i in visited :
#     print(i)




