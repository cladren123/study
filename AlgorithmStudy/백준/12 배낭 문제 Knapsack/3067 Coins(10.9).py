"""

문제유형 :
다이나믹 프로그래밍
배낭 문제

"""

import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test) :
    # n : 동전의 가지 수
    n = int(input())

    # 동전의 각 금액
    nlist = list(map(int, input().split()))

    # m : 동전으로 만들어야할 금액
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1

    for coin in nlist :
        for j in range(coin, m+1) :
            dp[j] += dp[j - coin]

    print(dp[m])




