"""

DP

????



"""
import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :

    n = int(input())

    dp = []


    # [0이 출력되는 횟수, 1이 출력되는 횟수]

    if n >= 0 :
        dp.append([1,0])
    if n >= 1 :
        dp.append([0,1])

    if n >= 2 :
        for i in range(2,n+1) :
            zero0 = dp[i-2][0]
            one0 = dp[i-2][1]
            zero1 = dp[i-1][0]
            one1 = dp[i-1][1]

            zero = zero0 + zero1
            one = one0 + one1

            dp.append([zero,one])

    print(dp[n][0], dp[n][1])







