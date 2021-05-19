n = int(input())

"""
점화식을
1과 2로 해당 숫자를 채우는 방법

n=1
1개

n=2 
2개

n=3 
1 1 1
1 2
2 1 
3개

n=4
1 1 1 1
1 1 2
1 2 1 
2 1 1
2 2
5개

n=5
1 1 1 1 1 1개
1 1 1 2  4개
1 2 2 3개
8개

점화식
dp[i] = dp[i-1] + dp[i-2]

"""

dp = [[] for i in range(n+1)]

if n >= 1:
    dp[1] = 1
if n >= 2 :
    dp[2] = 2
if n >= 3 :
    for i in range(3,n+1) :
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)



