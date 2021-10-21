
"""

거리 :
(r1, c1)  (r2, c2)
| r1 - r2 | + | c1 - c2 |

0. 궁수 배치 m의 3개
1. 궁수의 공격
2. 적이 이동

"""

import sys

input = sys.stdin.readline

# n : 행의 수, m : 열의 수, d : 궁수의 공격 거리 제한 d
n, m, d = map(int, input().split())

board = []
for _ in range(n) :
    one = list(map(int, input().split()))
    board.append(one)


answer = 0

visited = [0] * m
used = [0] * m

def dfs(stage) :
    # 종단조건
    if stage == 3 :
        print(used)
        pass

    for i in range(m) :
        if visited[i] == 0 :
            visited[i] = 1
            used[stage] = i
            dfs(stage+1)
            visited[i] = 0

dfs(0)





