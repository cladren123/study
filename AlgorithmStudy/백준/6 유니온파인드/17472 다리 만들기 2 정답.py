
"""
섬마다 연결도로를 구해서 union find??

다리의 길이 2이상
"""
from collections import deque

n,m = map(int, input().split())

board = []

for _ in range(n) :
    boardone = list(map(int, input().split()))
    board.append(boardone)

# for i in board :
#     print(i)


dx = [1,0,-1,0]
dy = [0,-1,0,1]

count = 1

que = deque()


for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 :
            count += 1
            board[i][j] = count
            que.append([i,j])

            while que :
                y,x = que.popleft()

                for k in range(4) :
                    nextx = x + dx[k]
                    nexty = y + dy[k]

                    if 0 <= nextx < m and 0 <= nexty < n and board[nexty][nextx] == 1  :
                        que.append([nexty, nextx])
                        board[nexty][nextx] = count




wire = []

for i in range(n) :
    for j in range(m) :
        if board[i][j] != 0 :

            for k in range(4) :
                y = i
                x = j
                cost = 0
                while True :
                    x += dx[k]
                    y += dy[k]
                    cost += 1


                    if 0 <= y < n and 0 <= x < m :
                        if board[y][x] == board[i][j]:
                            break
                        elif board[y][x] != 0  :
                            # print(j,i,x,y, cost-1)
                            wire.append([cost-1, board[i][j], board[y][x]])
                            cost = 0
                            break
                    else :
                        cost = 0
                        break


parent = [i for i in range(0, count+1)]
allcost = 0

def find(x) :
    if x == parent[x] :
        return x
    else :
        rootx = find(parent[x])
        parent[x] = rootx
        return parent[x]

def union(x,y) :
    rootx = find(x)
    rooty = find(y)

    if rootx != rooty :
        for i in range(len(parent)) :
            if parent[i] == rooty :
                parent[i] = rootx
        return 1
    else :
        return 0

wire.sort(key=lambda x:x[0])


for i in wire :
    start = i[1]
    end = i[2]
    costone = i[0]

    if costone <= 1 :
        continue
    else :
        check = union(start,end)
        if check == 1 :
            # print(costone, start, end)
            allcost += costone

answer = 0
numbercheck = 0
for i in parent :
    if i == parent[2] :
        numbercheck += 1


if numbercheck == count-1 :
    answer = allcost
else :
    answer = -1
#
# for i in board :
#     print(i)

# print()
# print(wire)
# print()
# print(parent)
# print(numbercheck)
print(answer)



