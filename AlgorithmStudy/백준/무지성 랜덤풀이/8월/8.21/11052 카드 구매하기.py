
"""

문제 유형 : DP

"""
import sys

input = sys.stdin.readline


n = int(input())

cardlist = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1,n+1) :
    dp[i] = cardlist[i]


for i in range(1,n+1) :
    for j in range(1,i) :
        dp[i] = max(dp[i], dp[i-j] + cardlist[j])

# print(dp)
print(dp[n])




