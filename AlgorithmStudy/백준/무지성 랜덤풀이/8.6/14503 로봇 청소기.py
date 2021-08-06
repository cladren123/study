import sys
from collections import deque

input = sys.stdin.readline

# n : 세로 크기, m : 가로 크기
n, m = map(int, input().split())

# r,c : 로봇청소기의 좌표, d : 바라보는 방향 0123 북동남서
r, c, d = map(int, input().split())


board = []


for _ in range(n) :
    one = list(map(int, input().split()))
    board.append(one)



dx = [0,1,0,-1]
dy = [-1,0,1,0]

visited = [[0] * (m) for _ in range(n)]

que = deque()

# r은 북쪽에서 떨어진 위치, c는 서쪽으로 부터 떨어진 위치
que.append([r,c,d])

# for i in board :
#     print(i)

visited[r][c] = 1
answer = 1

while que :
    y,x,d = que.popleft()

    flag = 0
    newd = d
    for i in range(4) :
        newd -= 1
        if newd < 0 :
            newd = 3

        nexty = y + dy[newd]
        nextx = x + dx[newd]

        if board[nexty][nextx] == 0 and visited[nexty][nextx] == 0 :
            que.append([nexty,nextx,newd])
            visited[nexty][nextx] = 1
            answer += 1
            flag = 1
            break

    if flag == 0 :
        backd = (d + 2) % 4

        backy = y + dy[backd]
        backx = x + dx[backd]

        if board[backy][backx] == 1 :
            break
        else :
            que.append([backy,backx,d])



print(answer)







