"""

문제 유형 : DP

p(n) : n일 때의 변의 길이인가?

1,1,1,2,2,3,4,5,7,9,12

dp[i] = dp[i-2] + dp[i-3]

"""
import sys

input = sys.stdin.readline


testcase = int(input())

for _ in range(testcase) :
    n = int(input())

    dp = [0] * (n+1)

    if n >= 1 :
        dp[1] = 1
    if n >= 2 :
        dp[2] = 1
    if n >= 3 :
        dp[3] = 1
    if n >= 4 :
        for i in range(4,n+1) :
            dp[i] = dp[i-2] + dp[i-3]

    print(dp[n])




