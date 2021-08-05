

import sys

input = sys.stdin.readline

n = int(input())
cur = input()
target = input()

# DP[숫자 나사 번호][왼쪽 회전수] = 최소 회전수

"""
오른쪽
dp[i][j] = min(dp[i][j], dp[i-1][j] + rcnt)

왼쪽
dp[i][(j+lcnt) % 10] = min(dp[i][(j+lcnt) % 10], dp[i-1][j] + lcnt)
"""

before = [0] * (n+1)
after = [0] * (n+1)


for i in range(n) :
    before[i+1] = int(cur[i])
    after[i+1] = int(target[i])


dp = [[sys.maxsize]*10 for _ in range(n+1)]

for i in range(10) :
    dp[0][i] = i



for i in range(1,n+1) :
    for j in range(10) :
        lcnt = (after[i] - before[i] - j + 20) % 10
        rcnt = 10 - lcnt

        dp[i][j] = min(dp[i][j], dp[i-1][j] + rcnt)
        dp[i][(j + lcnt) % 10] = min(dp[i][(j+lcnt) % 10], dp[i-1][j] + lcnt)



# for i in dp :
#     print(i)

answer = sys.maxsize
for i in range(10) :
    answer = min(answer, dp[n][i])

print(answer)





