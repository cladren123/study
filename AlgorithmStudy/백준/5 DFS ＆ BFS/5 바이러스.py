from collections import deque

computer = int(input())

n = int(input())

graph = [[0] * (computer + 1) for _ in range(computer+1)]


for i in range(n) :
    s,e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

visited = [0] * (computer+1)



que = deque()
que.append(1)
count = 0
answer = []
while que :
    cur = que.popleft()
    visited[cur] = 1

    for i in range(1,computer+1) :
        if graph[cur][i] == 1 and visited[i] == 0 :
            que.append(i)
            answer.append(i)

# print(set(answer))
print(len(set(answer)))








