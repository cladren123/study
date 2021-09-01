import sys

"""
1 = 1   -> 1
2 = 1+1, 2   ->   2
3 = 1+1+1, 2+1, 3, 1+2 -> 4
4 = 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1  -> 7 

"""



input = sys.stdin.readline

testcase = int(input())


for _ in range(testcase) :
    n = int(input())

    dp = [0] * (n+1)

    if n >= 1 :
        dp[1] = 1
    if n>=2 :
        dp[2] = 2
    if n>=3 :
        dp[3] = 4
    if n>=4 :
        for i in range(4,n+1) :
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[n])



