

n, m = map(int,input().split())

board = [list(input()) for i in range(n)]

count = 0

def solve(i,j) :
    global board
    count1 = 0
    count2 = 0
    check = board[i][j]
    for row in range(i, i+8) :
        for col in range(j, j+8) :
            if (row+col) % 2 == 0 :
                if board[row][col] == check :
                    count1 += 1
            elif (row+col) % 2 == 1 :
                if board[row][col] != check :
                    count1 += 1

    for row in range(i, i+8) :
        for col in range(j, j+8) :
            if (row+col) % 2 == 0 :
                if board[row][col] != check :
                    count2 += 1
            elif (row+col) % 2 == 1 :
                if board[row][col] == check :
                    count2 += 1
    low = min(count1, count2)
    return low


mini = 10000

for i in range(n-7) :
    for j in range(m-7) :
        mini = min(mini, solve(i,j))

print(mini)












