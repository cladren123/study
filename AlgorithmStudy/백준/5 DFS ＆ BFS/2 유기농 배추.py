
# m : 가로길이 n : 세로길이 k : 배추가 심어져 있는 위치의 개수
from collections import deque

testcase = int(input())

for _ in range(testcase) :
    m,n,k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k) :
        x,y = map(int, input().split()) #(x,y)
        board[y][x] = 1

    xway = [1,0,-1,0]
    yway = [0,-1,0,1]

    queue = deque()
    visited = [[0] * m for _ in range(n)]
    count = 0

    # board[y][x] x m y n

    for i in range(n) : # y
        for j in range(m) : # x
            if board[i][j] == 1 and visited[i][j] == 0 :
                queue.append((i,j))
                visited[i][j] = 1
                count += 1

                while queue :
                    y,x = queue.popleft()
                    for k in range(4) :
                        nextx = x + xway[k]
                        nexty = y + yway[k]
                        if 0 <= nextx < m and 0 <= nexty < n :
                            if board[nexty][nextx] == 1 and visited[nexty][nextx] == 0 :
                                queue.append((nexty, nextx))
                                visited[nexty][nextx] = 1


    # for i in visited :
    #     print(i)

    print(count)









