

"""

문제 유형 : DP 다이내믹프로그래밍

    1 2 3 4 5 6 7 8 9 10
1   1 2 2 3 4
2
5

1 : 1                               1
2 : 1+1, 2                          2
3 : 1+1+1, 1+2                      2
4 : 1+1+1+1, 1+1+2, 2+2             3
5 : 1+1+1+1+1, 1+1+1+2, 1+2+2, 5    5
6 : 1+1+1+1+1+1

참조
https://pacific-ocean.tistory.com/200

"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

worth = []

for _ in range(n) :
    worth.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1


# i는 동전의 가치
for i in worth :
    # j는 1~k 까지 각각의 경우의 수
    for j in range(1, k+1) :
        if j - i >= 0 :
            dp[j] += dp[j-i]

# print(dp)
print(dp[k])












