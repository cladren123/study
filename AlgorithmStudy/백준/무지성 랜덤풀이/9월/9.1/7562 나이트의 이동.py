
"""

문제 유형 : 그레프 이론

"""
import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :

    n = int(input())
    y,x = map(int, input().split())
    ty, tx = map(int, input().split())

    visited = [[0] * n for _ in range(n)]
    que = deque()

    # 나이트의 움직임
    dy = [2,1,-1,-2,-2,-1,1,2]
    dx = [1,2,2,1,-1,-2,-2,-1]

    que.append([y,x,0])

    visited[y][x] = 1

    answer = 0


    while que :
        y,x,count = que.popleft()

        if y == ty and x == tx :
            answer = count
            break

        for i in range(8) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n :
                if visited[ny][nx] == 0 :
                    visited[ny][nx] = 1
                    newcount = count + 1
                    que.append([ny,nx,newcount])
                if ny == ty and nx == tx :
                    que = []
                    answer = count + 1
                    break

    print(answer)

