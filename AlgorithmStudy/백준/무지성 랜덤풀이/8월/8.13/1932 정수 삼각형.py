import sys

input = sys.stdin.readline

"""
0
0 1 
0 1 2 
0 1 2 3 

"""

n = int(input())

graph = []

for _ in range(n) :
    graph.append(list(map(int, input().split())))


# for i in graph :
#     print(i)

for i in range(1,n) :
    for j in range(0,i+1) :

        if j == 0 :
            graph[i][j] = graph[i-1][j] + graph[i][j]
        elif j == i :
            graph[i][j] = graph[i-1][j-1] + graph[i][j]
        else :
            graph[i][j] = max(graph[i-1][j], graph[i-1][j-1]) + graph[i][j]

answer = max(graph[n-1])

print(answer)




