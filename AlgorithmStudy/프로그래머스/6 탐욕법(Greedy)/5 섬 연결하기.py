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

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]


# n = 5
# costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]

# n = 5
# costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]




def solution(n, costs):
    answer = 0

    # 비용이 적은 순으로 정렬
    costs.sort(key=lambda x: x[2])
    print(costs)

    visited = [0] * n

    costn = len(costs)

    costvisited = [0] * costn

    que = deque()
    que.append(costs[0])
    costvisited[0] = 1

    nodelist = []

    while True :
        print(que)
        s, e, c = que.popleft()
        visited[s] = 1
        visited[e] = 1

        nodelist.append(s)
        nodelist.append(e)
        nodelist1 = set(nodelist)
        nodelist = list(nodelist1)

        answer += c
        print(visited)
        print(nodelist)

        if 0 not in visited :
            break
        else :
            for i in range(1,costn) :
                if costvisited[i] != 1 :
                    if costs[i][0] in nodelist or costs[i][0] in nodelist or costs[i][1] in nodelist or costs[i][1] in nodelist :
                        if costs[i][0] in nodelist and costs[i][1] in nodelist :
                            continue
                        else:
                            # print(costs[i])
                            que.append(costs[i])
                            costvisited[i] = 1
                            break



    print(answer)
    return answer


solution(n,costs)