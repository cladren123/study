
"""



"""


import copy
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t) :

    n = int(input())

    graph = []

    for _ in range(2) :
        graph.append(list(map(int, input().split())))


    if n >= 2 :
        graph[0][1] = graph[1][0] + graph[0][1]
        graph[1][1] = graph[1][1] + graph[0][0]



    if n >= 3 :
        for i in range(2,n) :
            graph[0][i] += max(graph[1][i-1], graph[1][i-2])
            graph[1][i] += max(graph[0][i-1], graph[0][i-2])

    # for i in graph :
    #     print(i)

    print(max(graph[0][n-1], graph[1][n-1]))