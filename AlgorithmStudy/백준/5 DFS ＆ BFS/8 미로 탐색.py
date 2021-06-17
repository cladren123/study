# 실버 1
from collections import deque

n,m = map(int, input().split())

# 지린다.
board = [ list(map(int, input())) for _ in range(n)]

# print()
# for i in board :
#     print(i)

way_x = [1,0,-1,0]
way_y = [0,-1,0,1]

visited = [[-1] * m for _ in range(n)]
que = deque()

que.append((0,0,1))
visited[0][0] = 1



count = 1

while que :
    y,x,check = que.popleft()
    if check == count :
        count += 1


    for i in range(4) :
        next_y = y + way_y[i]
        next_x = x + way_x[i]
        if 0 <=next_x <m and 0 <=next_y <n :
            if board[next_y][next_x] == 1 and visited[next_y][next_x] == -1 :
                que.append((next_y,next_x,count))
                visited[next_y][next_x] = count



# print()
# for i in visited :
#     print(i)

print(visited[n-1][m-1])



