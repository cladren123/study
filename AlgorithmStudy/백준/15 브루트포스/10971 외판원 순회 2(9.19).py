"""

문제유형 :
브루트포스
백트래킹
외판원 순회 문제

모든 도시를 돌고 다시 자신의 도시로 와야 한다.
최소비용

출발도시가 안정해저 있는데..?

"""
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

# n : 도시의 개수 board : 도시의 길 정보
n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

# 모든 경우의 수를 구해 tlist에 담는다.
nlist = [i for i in range(n)]
tlist = list(permutations(nlist, n))

# 정답을 담을 변수 선언
answer = sys.maxsize

# 모든 경우의 수를 탐색
for case in tlist :
    money = 0
    case = list(case)

    # 모든 도시를 순회하고 처음 출발했던 도시로 와야하기 때문에 마지막에 처음 도시를 추가한다.
    case.append(case[0])

    for j in range(n) :
        # 도시의 길이 없는 경우 가장 큰 값을 더해서 정답 후보에서 제외시킨다.
        if  board[case[j]][case[j+1]] == 0 :
            money += sys.maxsize
        # 길이 있는 경우 비용을 더해 순회비용을 구한다.
        else :
            money += board[case[j]][case[j+1]]

    # 최소 순회 비용을 구한다.
    answer = min(answer, money)

print(answer)











