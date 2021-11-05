

import sys


input = sys.stdin.readline


# h : 세로  w : 가로
h, w = map(int, input().split())

board = [[0] * (w+1) for _ in range(h+1)]

blist = list(map(int, input().split()))

for i in range(w) :
    for k in range(blist[i]):
        board[h-k][i+1] = 1


answer = 0
check = 0
flag = 0

for i in range(h) :
    flag = 0
    check = 0
    for j in range(w) :
        garo = j+1
        sero = i+1

        if flag == 1:
            if board[sero][garo] == 1:

                answer += check
                check = 0

        if flag == 0 and board[sero][garo] == 1 :
            flag = 1

        if flag == 1 and board[sero][garo] == 0:
            check += 1



print(answer)





