

"""

문제 유형 : DP

"""
import copy
import sys


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

answer = 0

dp = [1] * n



for i in range(n) :
    for j in range(i) :
        if a[i] > a[j] :
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)
print(max(dp))









