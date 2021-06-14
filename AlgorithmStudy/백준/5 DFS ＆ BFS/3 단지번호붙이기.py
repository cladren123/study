from collections import deque

num = int(input())
board = []

for i in range(num) :
    an = input()
    board.append(an)

queue = deque()
visited = [[0] * num for i in range(num)]

xway = [1, 0, -1, 0]
yway = [0, -1, 0, 1]

count1 = 0
count2 = 0
answer = []

for nowy in range(num) :
    for nowx in range(num) :
        if board[nowy][nowx] == '1' and visited[nowy][nowx] == 0 :
            queue.append((nowy,nowx))
            count1 += 1
            visited[nowy][nowx] = count1
            count2 += 1


            while queue :
                y,x = queue.popleft()
                for i in range(4) :
                    nexty = y + yway[i]
                    nextx = x + xway[i]
                    if 0 <= nextx <= (num-1) and 0 <= nexty <= (num-1) :
                        if board[nexty][nextx] == '1' and visited[nexty][nextx] == 0 :
                            queue.append((nexty, nextx))
                            visited[nexty][nextx] = count1
                            count2 += 1
            answer.append(count2)
            count2 = 0

print(count1)
answer.sort()
for i in range(count1) :
    print(answer[i])

# for i in visited :
#     print(i)







