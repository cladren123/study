
# 딕셔너리 형태의 리스트를 이용해서 풀었더니 메모리 초과를 극복할 수 있었다.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

bt = [0] * (n+1)

# i번째 작업을 하면 다음 작업의 조건을 충족하는 리스트
nextbuild = [[] for _ in range(n+1)]

# i번째 작업을 하기 위한 작업
needbuild = [[] for _ in range(n+1)]

# i번째 작업의 차수
nindegree = [0] * (n+1)


# 입력단
for i in range(1, n+1) :
    one = list(map(int, input().split()))

    # 작업 시간
    bt[i] = one[0]

    # 작업을 하기 위한 필요한 작업의 총합수
    nindegree[i] += one[1]

    # 선행 작업과 작업을 하기 위한 필요한 작업의 리스트를 만들어준다.
    for j in range(2, one[1] + 2) :
        nextbuild[one[j]].append(i)
        needbuild[i].append(one[j])



que = deque()

# 선행 작업이 필요없는 작업을 que에 넣는다.
for i in range(1,n+1) :
    if needbuild[i] == [] :
        que.append(i)

# print(nindegree)



while que :
    cur = que.popleft()

    # 작업의 최소시간은 선행 작업 중 최고로 걸리는 시간과 자기 자신의 작업 시간을 더한 것이다.
    mbt = 0
    for i in needbuild[cur] :
        mbt = max(mbt, bt[i])
    bt[cur] = bt[cur] + mbt


    # 하나이 작업을 끝내면 다음 해야할 작업을 탐색하고 해당되는 선행 작업의 필요한 수를 -1 해준다.
    for j in nextbuild[cur] :
        nindegree[j] -= 1

        # 선행 작업의 갯수가 0인것은 작업할 수 있으니 que에 넣어준다.
        if nindegree[j] == 0 :
            que.append(j)

print(max(bt))










