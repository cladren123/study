

"""
다아나믹 프로그래밍

"""
import sys

input = sys.stdin.readline

n = int(input())

graph = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n) :
    for j in range(i) :
        if graph[j] < graph[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
print(max(dp))



