"""

문제 유형 : DP

1,4,9.19,16,25

26 루트 5.1

7 루트 2.6

answer = 0
while n >= 1 :
    sq = sqrt(n)
    sq = int(sq)
    n = n - sq**2
    answer += 1
print(answer)

DP를 활용해보자

"""
import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1) :
    for j in range(1,i) :
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1

print(dp[n])





