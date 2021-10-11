
from collections import deque
import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :
    # n : 문서, m : 타겟
    n,m = map(int, input().split());
    # 문서이 랭크
    nlist = list(map(int, input().split()))

    # 큐
    que = deque()

    # 큐에 문서의 번호와 랭크를 담는다.
    for i in range(n) :
        que.append([i,nlist[i]])

    # 정답을 담을 리스트
    alist = [0] * n
    count = 1

    while que :
        # 현재 큐에 가장 큰 우선순위를 구한다.
        bestteam = max(que, key=lambda x : x[1])
        bestrank = bestteam[1]

        number, rank = que.popleft()

        # 우선순위와 같으면 출력 후 alist의 순서 저장
        if rank == bestrank :
            alist[number] = count
            count += 1
        # 우선순위보다 작으면 뒤로 보내진다.
        else :
            que.append([number, rank])

    # 정답리스트에서 타겟 번호에 해당하는 인쇄 순서를 출력
    print(alist[m])

