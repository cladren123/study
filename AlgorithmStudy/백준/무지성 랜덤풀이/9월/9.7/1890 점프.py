
"""

문제 유형 : DP

결국 dfs를 써야 하나...

dfs를 써야 한다.

해결법
1. 처음에 dp를 -1로 설정한다
-1 : 길을 건들지도 않음. 0 : 한 번이라도 갔음 1 : 목적지에 도달했음

2. dfs 함수 생성
목적지에 도달하면 return 1 
건들이기라도 했으면 return dp[y][x]

그 다음 경로 탐색해서 dfs 재귀 실행

그 다음 마지막으로 return dfs[y][x]  -> none이 return 되는 것을 방지

"""

import sys
from collections import deque

input = sys.stdin.readline


n = int(input())

board = []

for _ in range(n) :
    board.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(n)]

def dfs(y,x) :
    if y == n-1 and x == n-1 :
        return 1
    if dp[y][x] != -1 :
        return dp[y][x]

    dp[y][x] = 0

    can = board[y][x]

    ny = y + can
    nx = x + can

    if ny < n :
        dp[y][x] += dfs(ny,x)

    if nx < n :
        dp[y][x] += dfs(y,nx)

    return dp[y][x]


print(dfs(0,0))

# for i in dp :
#     print(i)













