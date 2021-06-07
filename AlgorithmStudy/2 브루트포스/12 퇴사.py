

n = int(input())

t = [0]
p = [0]
dp = [0]

for i in range(n) :
    ti,pi = map(int, input().split())
    t.append(ti)
    p.append(pi)
    dp.append(0)

dp.append(0)

for i in range(n, -1, -1) :
    if t[i] + i - 1 > n :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(max(dp))






