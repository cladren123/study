"""

문제유형 :
그래프 이론
그래프 탐색
너비 우선 탐색

6% 초과
53% 틀렸다고 뜨네..
종단 조건으로 0을 만나면 while문을 끝내고 return 하라 했다.
하지만 0부터 시작하는 경우 0을 포함하는 에러가 발생했다.
-2로 초기화 하고 -1을 만나면 return 하도록 했다.

"""
import sys
from collections import deque

input = sys.stdin.readline

# n : 수빈, k : 동생
n, k = map(int, input().split())

maxnum = 100001

timelist = [-2] * maxnum
beforelist = [-2] * maxnum

que = deque()
que.append(n)
beforelist[n] = -1
timelist[n] = 0

while que :
    now = que.popleft()

    n1 = now*2
    n2 = now+1
    n3 = now-1

    if n1 < maxnum and timelist[n1] == -2 :
        timelist[n1] = timelist[now] + 1
        beforelist[n1] = now
        que.append(n1)

    if n2 < maxnum and timelist[n2] == -2 :
        timelist[n2] = timelist[now] + 1
        beforelist[n2] = now
        que.append(n2)

    if n3 >= 0 and timelist[n3] == -2 :
        timelist[n3] = timelist[now] + 1
        beforelist[n3] = now
        que.append(n3)

print(timelist[k])

answer = []
answer.append(k)
bnode = k

while True :
    bnode = beforelist[bnode]
    if bnode == -1 :
        break
    answer.append(bnode)

answer.reverse()
print(*answer)
