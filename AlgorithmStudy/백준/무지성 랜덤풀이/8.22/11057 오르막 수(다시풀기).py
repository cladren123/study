"""

문제 유형 : DP

dp[1]
0 1 2 3 4 5 6 7 8 9

dp[2]

0 1 2 3 4 5 6 7 8 9 = 10
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9
3 4 5 6 7 8 9
4 5 6 7 8 9
5 6 7 8 9
6 7 8 9
7 8 9
8 9
9

55

dp[i][j] 에서
i가 자릿수이고 j가 맨 끝(왼쪽)에 오는 숫자 일 때
그 앞에 올 수 있는 숫자는 j보다 같거나 작은 숫자이다.

i=2, 2면 _2 02, 12, 22 3개
i=3, 2면 _2 002, 012, 112, 022, 122, 222 6개




"""

import sys

input = sys.stdin.readline

n = int(input())


dp = [[0] * 10 for _ in range(n+1)]

for i in range(10) :
    dp[1][i] = 1

for i in range(1,n+1) : # 자릿수
    for j in range(10) : # 끝의 숫자
        for k in range(j+1) : # 끝의 숫자에 들어오는 숫자
            dp[i][j] += dp[i-1][k]

"""
dp[1][2] = dp[0][0] + dp[0][1] + dp[0][2]

"""

for i in dp :
    print(i)

print(sum(dp[n]) % 10007)





