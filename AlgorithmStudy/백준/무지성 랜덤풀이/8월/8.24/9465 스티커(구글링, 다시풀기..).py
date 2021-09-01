"""




"""
import copy
import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :

    n = int(input())

    graph = []

    for i in range(2) :
        one = list(map(int, input().split()))
        graph.append(one)

    dp = copy.deepcopy(graph)


    if n >= 2 :
        dp[1][1] = dp[1][1] + dp[0][0]

    if n >= 3 :
        dp[1][2] = dp[1][0] + dp[0][1] + dp[1][2]

    if n >= 4 :
        for i in range(3,n) :
            dp[1][i] = max(dp[1][i] + dp[0][i-1] + dp[1][i-2], dp[1][i] + dp[0][i-2] + dp[1][i-3])



    dp[1][-2] += dp[0][n-1]


    print(max(dp[1]))




