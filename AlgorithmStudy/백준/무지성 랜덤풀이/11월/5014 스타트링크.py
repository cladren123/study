
from collections import deque

import sys

input = sys.stdin.readline


# f : 총 층
# s : 강호가 있는 층
# g : 강호가 가고 싶은 층
# u : 위로 u층을 간다
# d : 아래로 d층을 간다

f,s,g,u,d = map(int, input().split())

# 한 번도 방문하지 않았다면 -1
flist = [-1] * (f+1)


que = deque();

# 시작 층, 그리고 버튼 count
que.append([s,0])
flist[s] = 0

while que :
    start, count = que.popleft()

    upstart = start + u
    downstart = start - d

    if upstart <= f and flist[upstart] == -1 :
        flist[upstart] = count + 1
        que.append([upstart, count + 1])

    if downstart > 0 and flist[downstart] == -1:
        flist[downstart] = count + 1
        que.append([downstart, count + 1])

answer = flist[g]



if answer == -1 :
    print("use the stairs")
else :
    print(answer)






