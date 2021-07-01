"""
    for i in costs:
        if 0 not in visited:
            break
        else:
            if visited[i[0]] == 1 and visited[i[1]] == 1:
                continue
            else:
                visited[i[0]] = 1
                visited[i[1]] = 1
                answer += i[2]

비용이 작은 순으로 정렬
섬이 연결되지 않는 것을 찾아 연결

가장 작은 비용을 연결

리스트에 담아서 풀어야 한다...

n=4,
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
answer = 4

n = 5
costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]
answr = 15

n = 5
costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
answr = 8

"""
from collections import deque

# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]


# n = 5
# costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]

n = 5
costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]


# 크루스칼 알고리즘 풀이

def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    print(ans)
    return ans


solution(n,costs)