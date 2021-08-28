"""

문제 유형 BFS, DFS

이번에는 DFS로 풀어보자.

가로, 세로, 대각선으로 연결되어 있다.



"""



import sys

input = sys.stdin.readline

sys.setrecursionlimit(10000)



def dfs(y,x) :
    visited[y][x] = 1

    for i in range(8) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < h and 0 <= nx < w :
            if board[ny][nx] == 1 and visited[ny][nx] == 0 :
                visited[ny][nx] = 1
                dfs(ny, nx)


while True :

    w, h = map(int, input().split())

    if w == 0 and h == 0 :
        break

    board = []

    for _ in range(h) :
        board.append(list(map(int, input().split())))

    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,-1,-1,-1,0,1,1,1]

    visited = [[0] * w for _ in range(h)]

    answer = 0

    for i in range(h) :
        for j in range(w) :
            if board[i][j] == 1 and visited[i][j] == 0 :
                visited[i][j] = 1
                dfs(i,j)
                answer += 1

    print(answer)















