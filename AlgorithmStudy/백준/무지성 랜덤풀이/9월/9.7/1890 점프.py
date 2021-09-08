
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


input = sys.stdin.readline

# 보드의 크기 입력
n = int(input())

# 입력값을 받기 위한 board 리스트 생성
board = []

# 보드 입력
for _ in range(n) :
    board.append(list(map(int, input().split())))

# 경로의 개수를 저장할 dp리스트 생성 /  -1은 아직 한 번도 탐색하지 않은 경로를 의미
dp = [[-1] * n for _ in range(n)]

# 정답으로 가는 경로를 알기 위해 dfs 함수
def dfs(y,x) :
    # 종단 조건
    # 정답에 도달하면 1을 리턴
    if y == n-1 and x == n-1 :
        return 1

    # 한 번이라도 탐색한 경로라면 현재값을 리턴
    if dp[y][x] != -1 :
        return dp[y][x]

    # 한 번이라도 탐색한 경로면 0으로 바꾼다.
    dp[y][x] = 0

    # 점프할 크기를 담고 있는 칸의 점수
    can = board[y][x]

    ny = y + can
    nx = x + can

    # 점프를 통해 다음 칸을 탐색 (범위를 벗어나지 않게 if문 사용)
    if ny < n :
        dp[y][x] += dfs(ny,x)

    if nx < n :
        dp[y][x] += dfs(y,nx)

    # 종단 조건에 걸리지 않았을 때 현재 위치의 dp 정보 리턴
    return dp[y][x]

# 정답이 담긴 0,0 위치 출력
print(dfs(0,0))

# for i in dp :
#     print(i)













