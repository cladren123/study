import sys

input = sys.stdin.readline

line1 = ' ' + input().rstrip()
line2 = ' ' + input().rstrip()

n1 = len(line1)
n2 = len(line2)

dp =[[0] * n2 for _ in range(n1)]

for i in range(1, n1) :
    for j in range(1, n2) :
        if line1[i] == line2[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for i in dp :
#     print(i)


print(dp[-1][-1])














