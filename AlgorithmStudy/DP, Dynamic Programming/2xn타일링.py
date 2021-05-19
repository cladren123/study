
n = int(input())

dp = [0 for _ in range(n+1)]

if n <= 3 :
    print(n)
else :
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[i]%10007)


"""
DP를 담을 배열을 선언
그 배열을 활용해 찾는다. 
전에 있던 경우가 현재에 영향을 준다. 
"""


