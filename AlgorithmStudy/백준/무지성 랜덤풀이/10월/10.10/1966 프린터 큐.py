
from collections import deque
import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) : 
    n,m = map(int, input().split());
    nlist = list(map(int, input().split()))
    que = deque()

    for i in range(n) :
        que.append([i,nlist[i]])

    alist = [0] * n
    count = 1

    while que :
        bestteam = max(que, key=lambda x : x[1])
        bestrank = bestteam[1]

        number, rank = que.popleft()

        if rank == bestrank :
            alist[number] = count
            count += 1
        else :
            que.append([number, rank])


    print(alist[m])

