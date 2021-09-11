
"""

문제 유형 : DP

"""
import sys

input = sys.stdin.readline

n = int(input())

nlist = []

for _ in range(n) :
    s,e = map(int, input().split())
    nlist.append([s,e])

# A 전봇대를 기준으로 정렬
nlist.sort()

# B의 가장 큰 오름차순 행렬을 구한다.
dp = [1] * n

for i in range(n) :
    for j in range(i) :
        if nlist[i][1] > nlist[j][1] :
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)
print(n - max(dp))



