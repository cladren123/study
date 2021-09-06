
"""

문제 유형 : DP

"""
import sys

input = sys.stdin.readline

n = int(input())

nl = list(map(int, input().split()))

dp = [1] * (n+1)

# 큰 것을 찾아서 +1 을 하면 된다.

for i in range(n) :
    for j in range(i) :
        if nl[i] < nl[j] :
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))