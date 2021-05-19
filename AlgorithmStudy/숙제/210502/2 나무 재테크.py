
# N = 배열의 줄 , 변의 길이
# M = 상도가 심은 나무의 정보를 나타내는 세 정수
# K = 년수

directX = [1,1,0,-1,-1,-1,0,1]
directY = [0,1,1,1,0,-1,-1,-1]

winterboard = []

N,M,K = map(int, input().split())

board = [[5] for i in range(N) for j in range(N)]

for i in range(N) :
    A = list(map(int, input().split()))
    winterboard.append(A)


tree = [[[] for i in range(N)] for j in range(N)]

for j in range(M) :
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

for i in tree :
    print(i)



print(tree)
print(len(tree[0][0]))

# 봄 + 여름
for i in range(N) :
    for j in range(N) :
        if tree[i][j] :
            print(tree[i][j])
            for k in range(len(tree[i][j])) :
                result = board[i][j] - tree[i][j][k]
                if result < 0 :
                    board[i][j] += tree[i][j][k] // 2
                    del tree[i][j][k]
                else :
                    board[i][j] -= tree[i][j][k]

# 가을
for i in range(N) :
    for j in range(N) :
        for k in range(len(tree[i][j])) :
            if tree[i][j][k] % 5 == 0 :
                for xdirect in directX :
                    for ydirect in directY :
                        if 0 <= i+xdirect <= N-1 and 0 <= j+directY <= N-1 :
                            tree[i+xdirect][j+ydirect].append(1)

# 겨울
for i in range(N) :
    for j in range(N) :
        board[i][j] += winterboard[i][j]

for i in board :
    print(i)
for j in tree :
    print(j)














                    














