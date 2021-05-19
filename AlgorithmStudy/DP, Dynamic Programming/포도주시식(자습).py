"""
가장 많은 포도주를 먹을 수 있는 방법!!
연속해서 3잔은 마실 수 없다.

6 10 13 9 8 1

dp[1]
drink[1]

dp[2]
dp[1] + drink[2]

dp[3]
drink[1] + drink[2]
drink[1] + drink[3]
drink[2] + drink[3]

dp[4]
drink[1] + drink[2] + drink[4] => dp[2] + drink[4]
drink[2] + drink[3] => dp[3]
drink[1] + drink[3] + drink[4] => dp[1] + drink[3] + drink[4]

dp[i] = dp[i-2] + drink[i] , dp[i-1] , dp[i-3] + drink[i-1] + drink[i]
"""

n = int(input())

drink = [0]

for i in range(n) :
    one = int(input())
    drink.append(one)

dp = [0 for i in range(n+1)]

if n >= 1 :
    dp[1] = drink[1]
if n >= 2 :
    dp[2] = drink[1] + drink[2]
# dp[3] = max(dp[2], drink[1]+drink[3], drink[2]+drink[3])
if n >= 3 :
    for i in range(3,n+1) :
        dp[i] = max(dp[i-2]+drink[i], dp[i-1], dp[i-3]+drink[i-1]+drink[i])
print(dp[n])

