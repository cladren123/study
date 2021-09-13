
"""

문제 유형 :
이분 탐색
누적합

"""
import sys

input = sys.stdin.readline

n,h = map(int, input().split())

board = []

# 석순, 종유석

for _ in range(n) :
    board.append(int(input()))

# print(board)

board1 = [0] * (h+1)
board2 = [0] * (h+1)




for i in range(n) :
    if i % 2 == 0 :
        board1[board[i]+1] -= 1
    else :
        board2[h - board[i]+1] += 1

# print(board1)
# print(board2)

# 0.5 ~ 6.5
dp = [0] * (h+1)
dp[0] = n//2

for i in range(1,h+1) :
    dp[i] = dp[i-1] + board1[i] + board2[i]

# print(dp)

del dp[-1]

answer1 = min(dp)
answer2 = dp.count(answer1)

print(answer1, answer2)





