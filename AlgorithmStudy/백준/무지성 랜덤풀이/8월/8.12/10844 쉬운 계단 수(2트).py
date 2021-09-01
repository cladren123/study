import sys

input = sys.stdin.readline

"""
0 1 2 3 4 5 6 7 8 9 

0 1 1 1 1 1 1 1 1 1   =   9

1 1 2 2 2 2 2 2 2 1   =   17

1 3 3 4 4 4 4 4 3 2   =   32 

대각선 위의 값들의 합 




"""



n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

for i in range(1,10) :
    dp[1][i] = 1

for i in range(2, n+1) :
    for j in range(10) :
        if j == 0 :
            dp[i][j] = dp[i-1][j+1]
        elif j == 9 :
            dp[i][j] = dp[i-1][j-1]
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# for i in dp :
#     print(i)

allsum = sum(dp[n]) % 1000000000

print(allsum)


