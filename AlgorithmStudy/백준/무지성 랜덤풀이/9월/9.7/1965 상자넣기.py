"""

문제 유형 : DP

"""
import sys

input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))

dp = [1] * n



for i in range(n) :
    for j in range(i) :
        if nl[i] > nl[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))