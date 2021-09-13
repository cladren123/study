"""

문제 유형 : DP, 누적합

"""
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
board = list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = board[1]

for i in range(1,n+1) :
    dp[i] = board[i-1] + dp[i-1]

# print(dp)

for _ in range(m) :
    s, e = map(int, input().split())

    answer = dp[e] - dp[s-1]

    print(answer)


