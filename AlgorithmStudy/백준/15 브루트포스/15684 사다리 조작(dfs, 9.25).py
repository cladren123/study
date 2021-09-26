"""

문제유형 :
구현
브루트포스
백트래킹

"""

import sys

input = sys.stdin.readline

# n : 세로선, m : 가로선, h : 세로선마다 가로선을 놓을 수 있는 위치
n, m, h = map(int, input().split())

graph = [[0] * (n+1) for _ in range(h+1)]

# 사다리 표시
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1


# 정답의 조건을 만족하는 확인
def check() :
    # 모든 세로선 탐색
    for i in range(n+1) :
        num = i
        for j in range(h+1) :
            if graph[j][num] == 1 :
                num += 1
            elif graph[j][num-1] == 1 :
                num -= 1
        if num != i :
            return False
    return True

answer = 5

# 탐색 0,1,2,3
# idx는 중복을 줄이는 역할을 한다. 
def dfs(stage, idx, linenumber) :
    global answer

    # 종단조건
    if stage == linenumber :
        if check():
            answer = min(answer, linenumber)
        return

    # 기존에 탐색했던 줄은 탐색하지 않는다. idx
    for i in range(idx,h+1) :
        for j in range(1,n+1) :
            if j+1 < n+1 :
                if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i][j+1] == 0 :
                    graph[i][j] = 1
                    dfs(stage+1, i, linenumber)
                    graph[i][j] = 0

# 0~3까지의 경우의 수를 탐색
for i in range(4) :
    dfs(0,1,i)

# 정답이 없을 경우 -1로 출력
if answer == 5 :
    answer = -1

print(answer)
