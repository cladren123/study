"""

문제 유형 : DFS, BFS

"""
import copy
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

t1, t2 = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

# s : 부모 e : 자식

for _ in range(m) :
    s,e = map(int, input().split())
    # 자식이 부모를 가지고 있다.
    graph[e].append(s)
    graph[s].append(e)

# for i in graph :
#     print(i)

# BFS와 DFS 둘 다 풀 수 있을 거 같다.

# BFS

que = deque()

moum = []
moum.append(t1)

que.append([t1, 0, moum])

answer = -1

while que :
    cur, count, moum = que.popleft()


    for i in graph[cur] :
        if i == t2 :
            answer = count + 1
            break

        if i in moum :
            continue
        else :
            newmoum = copy.deepcopy(moum)
            newmoum.append(i)
            que.append([i, count+1, newmoum])


print(answer)















