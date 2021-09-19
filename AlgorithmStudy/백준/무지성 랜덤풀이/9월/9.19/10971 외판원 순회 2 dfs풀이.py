import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

minvalue = sys.maxsize

def dfs(start, next, value, visited) :
    global minvalue

    # 종단 조건
    if len(visited) == n :
        if board[next][start] != 0 :
            minvalue = min(minvalue, value + board[next][start])
        return

    # dfs 탐색
    # i는 다음에 탐색할 도시
    for i in range(n) :
        if board[next][i] != 0 and i not in visited and i != start :
            visited.append(i)
            # 새로 선언하는게 중요하다. value += board[next][i] 중복되버린다.
            newvalue = value + board[next][i]
            dfs(start, i, newvalue, visited)
            visited.pop()

for i in range(n) :
    dfs(i, i, 0, [i])

print(minvalue)