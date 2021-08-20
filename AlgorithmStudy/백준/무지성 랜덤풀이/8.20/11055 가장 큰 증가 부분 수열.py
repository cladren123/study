"""

문제 유형 = DP

"""
import sys

input = sys.stdin.readline


# n : 수열의 크기
n = int(input())

# 수열
nlist = list(map(int, input().split()))

dp = [0] * n

for i in range(n) :
    start = 0
    allsum = 0
    for j in range(i) :
        if nlist[j] < nlist[start] :
            continue
        else :
            allsum += nlist[j]
            start = j
    if allsum >= max(dp) :
        dp[i] = allsum
    else :
        dp[i] = max(dp)

print(dp)
print(max(dp))




