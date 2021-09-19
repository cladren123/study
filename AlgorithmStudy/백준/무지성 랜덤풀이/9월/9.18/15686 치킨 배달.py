
"""

문제유형 :
구현
브루트포스

치킨 거리 :
집과 가장 가까운 치킨집 사이의 거리
집을 기준
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

M 개를 고르고 나머지 폐업
도시의 치킨 거리가 가장 작게 될지 구하는 프로그램 작성

"""
import sys
from itertools import combinations

input = sys.stdin.readline

# n 정사각형의 한 번, m 최대 치킨집의 수
n, m = map(int, input().split())

board = []

for _ in range(n) :
    board.append(list(map(int, input().split())))


# 집의 위치를 저장하는 리스트
home = []

# 가게의 위치를 저장하는 리스트
store = []

for i in range(n) :
    for j in range(n) :
        # 1 은 집
        if board[i][j] == 1 :
            home.append([i,j])
        # 2 는 치킨집
        if board[i][j] == 2 :
            store.append([i,j])

# 전체 가게의 개수 중 m개의 가게의 경우의 수를 구한다.
choose = list(combinations(store,m))

answer = sys.maxsize
guri = 0

# 경우의 수마다 치킨거리를 구하고 그 중 가장 작은 것을 정답으로 출력해야 한다.
# 치킨거리를 구하기 위해서 가게와 집의 모든 거리를 구한 후 작은 거리를 찾은 다음 더해야 한다.
# case : 제거 되고 남은 가게가 있는 경우
for case in choose :
    chickenguri = 0
    for h1 in home :
        minguri = sys.maxsize
        for gage in case:
            guri = abs(h1[0] - gage[0]) + abs(h1[1] - gage[1])
            minguri = min(minguri, guri)
        chickenguri += minguri
    answer = min(answer, chickenguri)

print(answer)










