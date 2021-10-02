"""

문제유형 :
그래프 이론
그래프 탐색
트리
깊이 우선 탐색

"""


import sys

sys.setrecursionlimit(10000);
input = sys.stdin.readline;

# 트리에서 어떤 두 노드를 선택해 최고 길이를 구하라

# 입력단
# n : 노드 개수
n = int(input())

graph = [[] for _ in range(n+1)];

# 입력받은 가중치를 담은 함수
weight = [0] * (n+1)

# 확인용
# maxweight : 각 노드의 가장 큰 지름
maxweight = [0] * (n+1)
# maxworth : 부모 노드한테 보내는 가장 큰 가중치
maxworth = [0] * (n+1)

for _ in range(n-1) :
    parent, son, worth = map(int, input().split())
    graph[parent].append(son)
    weight[son] = worth

answer = 0

def dfs(node) :
    global answer;

    # 종단조건, 리프노드 일 때
    if len(graph[node]) == 0 :
        return weight[node]
    # 리프노드가 아닐 때
    else :
        weightlist = []

        # 연결된 간선에서 최고 가중치를 받아서 저장한다.
        for nextnode in graph[node] :
            weightlist.append(dfs(nextnode));

        # 내림차순 정렬로 인해 가증 큰 값을 찾는다.
        weightlist.sort(reverse=True)

        # 자식 노드가 2개 이상일 때 가장 큰 두개의 합을 구한다.
        if len(weightlist) >= 2 :
            checksum = weightlist[0] + weightlist[1]
        # 자식 노드가 하나일 때
        else :
            checksum = weightlist[0]



        # 최고 가중치 2개의 합을 정답과 비교해 큰 값을 찾는다.
        answer = max(answer, checksum)

        # 부모 노드로 가중치를 보낼 때 가장 큰 값을 보낸다.
        maxweight[node] = sum(weightlist)
        maxworth[node] = weight[node] + max(weightlist)
        return weight[node] + max(weightlist)

dfs(1)

# print(maxweight)
# print(maxworth)

print(answer)























