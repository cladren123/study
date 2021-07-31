import sys
from collections import deque

input = sys.stdin.readline

# 몇 번 테스트 할 건지 입력
testcase = int(input())
for _ in range(testcase) :

    # n 건물수, k 선행 건물 조건 갯수 기입
    n, k = map(int, input().split())

    # 건물을 짓는데 걸리는 시간
    d = [0] + list(map(int, input().split()))

    # 선행 건물의 조건을 나타내는 그래프.
    # 가로로 읽으면 이 건물을 지으면 다음에 지을 수 있는 건물, 세로로 읽으면 이 건물을 짓기 위해서 필요한 건물이 뭔지 알 수 있다.
    graph = [[0] * (n+1) for _ in range(n+1)]

    # 선행 건물의 갯수를 알려주는 리스트
    nd = [0] * (n+1)

    for _ in range(k) :
        s, e = map(int, input().split())
        graph[s][e] = 1
        nd[e] += 1

    # 목표 건물
    w = int(input())

    que = deque()

    # 선행 건물이 0인 처음에 지을 수 있는 건물을 que에 넣는다.
    for i in range(1, n+1 ) :
        if nd[i] == 0 :
            que.append(i)

    # 정답리스트, 각 건물마다 짓는데 필요한 최소 건물 시간을 넣는다.
    alist = [0] * (n+1)

    # for i in graph :
    #     print(i)
    # print(nd)

    while que :
        cur = que.popleft()

        # newbt에 현재 건물을 짓기 위해서 선행과정의 건물 중 가장 오래 걸리는 시간을 찾는다. (조건을 채우기까지 필요한 시간)
        # newbt와 그 건물을 짓는 시간을 더해서 정답리스트 alist에 넣는다.
        newbt = 0
        for i in range(1,n+1) :
            if graph[i][cur] == 1 :
                newbt = max(newbt, alist[i])

        nowbt = newbt + d[cur]
        alist[cur] = nowbt

        # 이 건물을 지으면 다음에 지을 수 있는 건물에 선행차수 -1을 한다.
        # 선행차수 nd가 0 이면 que에 넣는다.
        for j in range(1, n+1) :
            if graph[cur][j] == 1 :
                nd[j] -= 1

                if nd[j] == 0 :
                    que.append(j)


    # 목표 건물의 최소 건물 시간을 출력한다.
    print(alist[w])






















