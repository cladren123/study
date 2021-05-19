"""
2579번 계단 오르기
연속된 세 개의 계단을 모두 밟아서는 안된다. 시작점은 계단에 미포함
마지막 도착 계단은 반드시 밟아야 한다.
한 단계 또는 두 단계씩 오를 수 있다.

dp 1
s1

dp 2
s1 + s2

dp 3
s1 + s3
s2 + s3

dp 4
s1 + s2 + s4 = dp2 + s4
s1 + s3 + s4
s2 + s4


dp 5
s1 + s2 + s4+ s5 = dp2 + s4 + s5
s1 + s3 + s5 = dp3 + s5
s2 + s3 + s5 =

dp[i] = dp[i-3] + s[i-1] + s[i]
dp[i] = dp[i-2] + s[i]
"""

n = int(input())

s = [0]
dp = [0 for i in range(n+1)]

for i in range(n) :
    sta = int(input())
    s.append(sta)

# print(s)


"""
dp[i] = dp[i-3] + s[i-1] + s[i]
dp[i] = dp[i-2] + s[i]
"""
if n >= 1 :
    dp[1] = s[1]
if n >= 2 :
    dp[2] = s[1] + s[2]
if n >= 3 :
    for i in range(3,n+1) :
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

# print(dp)

print(dp[n])

