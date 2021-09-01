"""
깊이 우선 탐색 - DFS 인데 bfs로 풀을래


"""
import copy
import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())


def bfs(start):

    que = deque()
    que.append(start)
    visited[start] = 1


    while que:
        cur = que.popleft()
        nownum = visited[cur]

        for nextv in graph[cur]:
            if visited[nextv] == 0:
                if visited[cur] == 1:
                    visited[nextv] = 2
                    que.append(nextv)
                elif visited[cur] == 2:
                    visited[nextv] = 1
                    que.append(nextv)
            else:
                if visited[nextv] == nownum:
                    return False

    return True


for _ in range(testcase) :
    v, e = map(int, input().split())

    flag = 0

    graph = [[] for _ in range(v+1)]
    visited = [0] * (v + 1)

    for _ in range(e) :
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, v+1) :
        if visited[i] == 0 :
            if bfs(i) == False :
                flag = 1
                break

    if flag == 1 :
        print("NO")
    else :
        print("YES")








