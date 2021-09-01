
"""

문제 유형 : DFS

시간초과발생..

DFS로 푸니까 시간초과나 메모리초과가 발생한다...

상황에 따라 BFS냐, DFS냐 를 잘 선택해야 한다.

"""
import sys

sys.setrecursionlimit(1000000000)

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,e = map(int, input().split())
    graph[e].append(s)



def dfs(node) :
    global count
    for i in graph[node] :
        if visited[i] == 0 :
            visited[i] = 1
            count += 1
            dfs(i)


answer = []

maxnum = 0

result = []

for i in range(1,n+1) :
    visited = [0] * (n+1)
    count = 0
    visited[i] = 1
    dfs(i)

    if count > maxnum :
        result = [i]
        maxnum = count
    elif count == maxnum :
        result.append(i)

for i in result :
    print(i, end = " ")















