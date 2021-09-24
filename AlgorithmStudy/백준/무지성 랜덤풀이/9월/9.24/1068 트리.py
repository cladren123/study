"""

문제유형 :
그래프 이론
그래프 탐색
트리
깊이 우선 탐색

"""
import sys

input = sys.stdin.readline

n = int(input())
nroot = list(map(int, input().split()))
dnode = int(input())

# 리프 노드의 개수 출력
# 더 이상 탐색할 수 없을 때

answer = 0
root = 0

for i in range(n) :
    if nroot[i] == -1 :
        root = i

graph = [[] for _ in range(n)]

# 다음 노드로 갈 수 있는 정보 저장
for i in range(n) :
    if nroot[i] == -1 :
        continue
    graph[nroot[i]].append(i)



# 노드 제거
for i in graph :
    if dnode in i :
        i.remove(dnode)
graph[dnode].clear()


def dfs(node) :
    global  answer
    # 종단조건
    if len(graph[node]) == 0 :
        answer += 1

    else :
        for nextnode in graph[node] :
            dfs(nextnode)

dfs(root)

if dnode == root :
    answer = 0

print(answer)








