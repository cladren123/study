import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :

    n, k = map(int, input().split())

    d = [0] + list(map(int, input().split()))

    graph = [[0] * (n+1) for _ in range(n+1)]
    nd = [0] * (n+1)

    for _ in range(k) :
        s, e = map(int, input().split())
        graph[s][e] = 1
        nd[e] += 1

    w = int(input())

    que = deque()

    for i in range(1, n+1 ) :
        if nd[i] == 0 :
            que.append(i)

    alist = [0] * (n+1)

    # for i in graph :
    #     print(i)
    # print(nd)

    while que :
        cur = que.popleft()

        newbt = 0
        for i in range(1,n+1) :
            if graph[i][cur] == 1 :
                newbt = max(newbt, alist[i])

        nowbt = newbt + d[cur]
        alist[cur] = nowbt

        for j in range(1, n+1) :
            if graph[cur][j] == 1 :
                nd[j] -= 1

                if nd[j] == 0 :
                    que.append(j)


    print(alist[w])






















