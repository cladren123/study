"""

문제 유형 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트랙킹

백트랙킹이랑 DFS라 곂치는게 많은 거 같다..? BFS로는 부족함

BFS 로 하니까 메모리초과 발생..

"""
import copy
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

board = []

for _ in range(R) :
    board.append(list(input().strip()))

# print(board)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

# BFS

# 메모리 초과와 시간 초과를 해결하기 위해 set을 사용한다.



que = set([(0,0, board[0][0])])

# 개인 알파를 가저야한다.

answer = 1

while que :
    cury, curx, alpa = que.pop()

    for i in range(4) :
        nexty = cury + dy[i]
        nextx = curx + dx[i]

        if 0 <= nexty < R and 0 <= nextx < C :
            if board[nexty][nextx] not in alpa :
                que.add((nexty, nextx, alpa + board[nexty][nextx]))
                answer = max(answer, len(alpa) + 1)


print(answer)









