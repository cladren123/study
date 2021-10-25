"""

문제유형 :
브루트포스 알고리즘
백트래킹

n개의 퀸 배치
무조건 한 행, 한 열에는 퀸이 있어야 한다.


"""
import sys

input = sys.stdin.readline

n = int(input())

row = [0] * n
answer = 0

def adjacent(x) :
    for i in range(x) :
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i :
            return False
    return True

def dfs(x) :
    global answer

    if x == n :
        answer += 1
    else :
        for i in range(n) :
            row[x] = i
            if adjacent(x) :
                dfs(x+1)

dfs(0)
print(answer)













