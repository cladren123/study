"""

문제유형 :
누적합

"""
import sys

input = sys.stdin.readline


n = int(input())
nlist = list(map(int, input().split()))
m = int(input())

dp = [0] * (n+1)
dp[1] = nlist[0]

# 누적합 dp 만들기
for i in range(2,n+1) :
    dp[i] = dp[i-1] + nlist[i-1]

for _ in range(m) :
    s,e = map(int, input().split())

    answer = dp[e] - dp[s-1]
    print(answer)














