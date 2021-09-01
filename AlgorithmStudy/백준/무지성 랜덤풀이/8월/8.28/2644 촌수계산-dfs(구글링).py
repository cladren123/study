import sys

input = sys.stdin.readline


n = int(input())
t1, t2 = map(int, input().split())

m = int(input())

graph =[[] for _ in range(n+1)]

for _ in range(m) :
    s,e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)

# 굳이 return을 쓰지 않아도 된다.

# visited를 채워가는 과정 

def dfs(before) :
    for i in graph[before] :
        if i != t1 and visited[i] == 0 :
            visited[i] = visited[before] + 1
            dfs(i)

dfs(t1)

print(visited)

if visited[t2] == 0 :
    print(-1)
else :
    print(visited[t2])




