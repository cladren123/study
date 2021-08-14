"""
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만,
마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다.
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

N 학생수
M 키를 비교한 횟수

1,3

1이 3보다 앞선다.

"""




from collections import deque

N, M = map(int, input().split())

# graph는 N+1개 만큼자리를 만든다. 1부터 시작하기 위해서 N+1
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)


# 뒤에 서야 하는 것들을 graph[a]에 해당하는 b를 넌다.
# 뒤에 서는 b에 1을 추가한다.
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


print(graph)
print(indegree)

# i가 0 이면 queue를 추가한다. 아마 가장 앞에 서는 친구일듯
queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    print(cur)
    print(graph[cur])
    for i in range(len(graph[cur])):
        next = graph[cur][i]
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)