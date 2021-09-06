"""

dp = 1 / 1
1

dp = 2 / 2
00
11

dp = 3 / 3
100
001
111

dp[3] = dp[1] + dp[2]

dp = 4 / 5
0000
1100

1001
0011
1111

dp[4] = dp[2] + dp[3]


"""


import sys

input = sys.stdin.readline


number = 15746

n = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1) :
    dp[i] = (dp[i-1] + dp[i-2]) % number

print(dp[n])