
"""

문제 유형 : DP

1 0 1 1
2 0 2 1 2 2
3 0 3 1 3 2 3 3
4 0 4 1 4 2 4 3 4 4
5 0 5 1 5 2 5 3 5 4 5 5



1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

n <= 1000



"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (i+1) for i in range(1001)]

for i in range(1,1001) :
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(2, 1001) :
    for j in range(1,i) :
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] % 10007


# for i in range(1,5) :
#     print(dp[i])

print(dp[n][k] % 10007)






