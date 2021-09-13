
"""

문제 유형 : DP, 누적합

"""
import sys

input= sys.stdin.readline

n,m = map(int, input().split())

board = []
graph = []

for _ in range(n) :
    board.append(list(map(int, input().split())))

for _ in range(m) :
    graph.append(list(map(int, input().split())))

dp = [[0] * (n+1) for _ in range(n+1)]
dp[1][1] = board[0][0]

for i in range(1,n+1) :
    for j in range(1,n+1) :
        dp[i][j] = board[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# for i in dp :
#     print(i)

for y1,x1,y2,x2 in graph :
    answer = dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]
    print(answer)



