"""

DP


"""
import sys

input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))


dp = [-1001] * n
dp[0] = numlist[0]


for i in range(1,n) :
    dp[i] = max(numlist[i], dp[i-1] + numlist[i])


print(max(dp))