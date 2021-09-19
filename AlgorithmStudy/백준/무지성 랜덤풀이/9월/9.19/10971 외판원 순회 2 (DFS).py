"""

출저 :
https://www.acmicpc.net/problem/10971

n과 m
dfs 형식
브루트포스 알고리즘

"""


import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

minvalue = sys.maxsize

def dfs(start, next, value, visited) :
    global minvalue

    if len(visited) == n :
        if board[next][start] != 0 :
            minvalue = min(minvalue, value + board[next][start])
        return

    for i in range(n) :
        if board[next][i] != 0 and i != start and i not in visited :
            visited.append(i)
            dfs(start, i, value + board[next][i], visited)
            visited.pop()


for i in range(n) :
    dfs(i, i, 0, [i])

print(minvalue)



