"""
깊이 우선 탐색 - DFS


"""
import copy
import sys

input = sys.stdin.readline

v, e = map(int, input().split())

visited = [0] * (v + 1)

graph = [[0] * (v+1) for _ in range(v+1)]

for _ in range(e) :
    start, end = map(int, input().split())

    graph[start][end] = 1
    graph[end][start] = 1


for i in graph :
    print(i)


def dfs(node) :
    global v, graph

    visited[node] = 1
    print(node, end = " ")

    for i in range(1, v+1) :
        if graph[node][i] == 1 and visited[i] == 0 :
            dfs(i)



























