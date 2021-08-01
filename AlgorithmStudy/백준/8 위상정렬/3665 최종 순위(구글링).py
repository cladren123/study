
# 출저 : https://enjoyso.tistory.com/139


import sys
from collections import deque, defaultdict

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :

    n = int(input())

    rank = list(map(int, input().split()))

    # 딕셔너리를 사용하자
    graph = defaultdict(list)
    indegree = defaultdict(int)


    for i in range(n-1) :
        graph[rank[i]] = rank[i+1:]
        indegree[rank[i+1]] = i+1


    # m개의 상대순위 변동
    m = int(input())

    for _ in range(m) :
        a,b = map(int, input().split())

        if b in graph[a] :
            graph[b].append(a)
            graph[a].remove(b)

            indegree[a] += 1
            indegree[b] -= 1
        else :
            graph[a].append(b)
            graph[b].remove(a)

            indegree[a] -= 1
            indegree[b] += 1

    p = []

    for c in rank :
        if indegree[c] == 0 :
            p.append(c)

    ans = []

    while p :
        cur = p.pop()
        ans.append(cur)

        for i in graph[cur] :
            indegree[i] -= 1

            if indegree[i] == 0 :
                p.append(i)

    # *을 쓰면 [] 을 벗어나나 보다.
    if len(ans) == n :
        print(*ans)
    else :
        print("IMPOSSIBLE")


