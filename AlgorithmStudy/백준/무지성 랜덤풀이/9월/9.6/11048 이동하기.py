"""

문제 유형 : DP

"""
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

board = [[0] * (m+1)]

for _ in range(n) :
    one = [0] + list(map(int, input().split()))
    board.append(one)

dp = [[0] * (m+1) for _ in range(n+1)]



for i in range(1,n+1) :
    for j in range(1,m+1) :
        if i == 1 and j== 1 :
            dp[i][j] = board[i][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + board[i][j]

print(dp[n][m])