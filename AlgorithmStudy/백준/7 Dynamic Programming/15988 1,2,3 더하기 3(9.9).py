
"""

문제 유형 : DP

dp 1
1

dp 2
1+1
2

dp 3
1+1+1
2+1
3
1+2

dp 4
1+1+1+1
2+1+1
3+1
1+2+1
1+1+2
2+2
1+3

"""
import sys

input = sys.stdin.readline

number = 1000000009
testcase = int(input())

for _ in range(testcase) :
    n= int(input())
    dp = [0] * (n+1)
    if n >= 1 :
        dp[1] = 1
    if n >= 2 :
        dp[2] = 2
    if n >= 3 :
        dp[3] = 4

    for i in range(4, n+1) :
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % number

    print(dp[n]%number)