"""

문제 유형 : DP, N과 M

조합을 사용하면 편하다. -> 메모리 초과 발생

for _ in range(testcase) :
    n,m = map(int, input().split())


    listm = [i for i in range(m)]

    answer = len(list(combinations(listm, n)))
    print(answer)

0 < N <= M 30

4 3 2 1

1  2  3  4  5  6
0  1  3  6  10 15
"""
import sys
from itertools import combinations

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :
    n,m = map(int, input().split())

    dp = [[0] * 31 for i in range(31)]

    # dp[n][m]

    for j in range(31) :
        dp[1][j] = j

    for i in range(2,31) :
        for j in range(i,31) :
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    print(dp[n][m])




