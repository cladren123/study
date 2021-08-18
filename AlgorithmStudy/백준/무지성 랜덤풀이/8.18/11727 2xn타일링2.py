"""

문제 유형 : DP

2 1 / 1 2 / 2 2

n = 1
dp = 1

n = 2
dp = 3

n = 3
dp = 6

dp[n] = dp[n-2]*2 + dp[n-1] * 2

"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

if n >= 1 :
    dp[1] = 1
if n >= 2 :
    dp[2] = 3
if n >= 3 :
    for i in range(3,n+1) :
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

