import heapq
import sys

input = sys.stdin.readline

# v 정점의 개수, e 간선의 개수
v,e = map(int, input().split())

# 시작 정점의 번호
k = int(input())

# 간선의 정보를 저장할 리스트
graph = [[] for _ in range(v + 1)]

# 간선의 입력받아서 간선의 연결 정보를 담을 graph를 만든다.
for _ in range(e) :
    s, e, w = map(int, input().split())

    graph[s].append([w, e])


# 최소값을 뽑는 heap 자료형 생성
heap = []

# heap 리스트를 heap 자료형으로 만들면서 [0, 시작점] 을 넣어준다 [가중치, 시작점] 순서이다.
heapq.heappush(heap, [0,k])

# 정답을 담을 가중치 리스트의 초기값은 최대값한다. 비교를 통해 작은 값을 넣기 위해서
answerlist = [sys.maxsize] * (v+1)

# 시작점의 가중치는 0으로 만든다.
answerlist[k] = 0

while heap :
    # heap에 저장된 [가중치,노드] 를 빼낸 변수에 집어넣는다.
    cost, cur = heapq.heappop(heap)

    # 현재 answerlist의 값과 비교해 가중치가 더 큰 비용이면 무시한다.
    if answerlist[cur] < cost :
        continue

    # heap에서 꺼낸 노드가 갈 수 있는 노드를 탐색한다.
    for ncost, nextnode in graph[cur] :

        # 현재 노드에서 갈 수 있는 노드의 비용을 계산한다.
        nextcost = cost + ncost

        # 갈 수 있는 노드로 가능 비용이 기존의 것보다 크면 무시한다.
        if nextcost < answerlist[nextnode] :

            # 작은 값이면 정답리스트의 해당 노드의 가중치를 작은 값으로 넣어준다.
            answerlist[nextnode] = nextcost

            # 작은 값이 들어왔으면 heap 리스트에 넣어준다.
            heapq.heappush(heap, (nextcost, nextnode))


for i in range(1,v+1) :
    if answerlist[i] == sys.maxsize :
        print("INF")
    else :
        print(answerlist[i])
