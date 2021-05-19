
"""
점화식을 짜는 것이 중요하다.
"""

# DP로 중복을 제거한다.
# 11번을 돌린 결과와 1번 돌린 결과는 같다.
# 왼쪽으로 돌리면 모든 나사는 같이 따라서 돌게 된다.
# 오른쪽으로 돌리면 다른 나사는 함께 돌지 않는다.

# DP[숫자 나사 번호][왼쪽 회전수] = 최소 회전수수



n = int(input())
a = str(input())
b = str(input())

start = []
after = []

for i in range(n) :
    start.append(int(a[i]))
    after.append(int(b[i]))


dp = [[[] for i in range(10005)] for j in range(10)]

for i in range(10) :
    dp[0][i] = i;


leftcount = 0
rightcount = 0

for i in range(n) :
    for j in range(10) :
        leftcount = int((after[i] - j - start[i] + 20) % 10)
        rightcount = int(10 - leftcount)
        dp[i][j] = min(dp[i][j], dp[i-1][j] + rightcount)
        dp[i][(j+leftcount)%10]=min(dp[i][(j+leftcount)%10], dp[i-1][j] + leftcount);

#1e9 = 1*109 = 1000000000, 주로 무한대를 나타낼려고 사용한다.
ans = 1e9;

for i in range(10) :
    ans = min(ans, dp[n][i])

print(ans)













