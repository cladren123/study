
from collections import deque
import sys

input = sys.stdin.readline

# n : 보드의 크기
n = int(input())

# k : 사과의 개수
k = int(input())

klist = []
for _ in range(k) :
    klist.append(list(map(int, input().split())))

# l : 방향 변환 정보
l = int(input())

llist = deque()
for _ in range(l) :
    # 숫자도 문자로 입력되어 버렸다.
    t, d = input().split()
    t = int(t)
    llist.append([t,d])

board = [[0] * (n+1) for _ in range(n+1)]

# 사과배치
for y,x in klist :
    board[y][x] = 1

# 시계 방향
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 몸 길이
body = deque()
body.append([1,1])

# 처음 시작 방향 오른쪽
d = 0

# 시간을 센다
answer = 0

while True :
    # 머리 이동
    hy,hx = body[0][0], body[0][1]

    nhx = hx + dx[d]
    nhy = hy + dy[d]

    answer += 1

    # 범위안에서, 몸이 아니면 이동한다
    if 1 <= nhy < (n+1) and 1 <= nhx < (n+1) and [nhy,nhx] not in body:
        # 사과가 있으면 몸이 늘어나고 0으로 바꾼다.
        if board[nhy][nhx] == 1 :
            body.appendleft([nhy,nhx])
            board[nhy][nhx] = 0
        # 사과가 없으면 이동
        else :
            body.appendleft([nhy,nhx])
            body.pop()
    else :
        break

    # 방향 전환
    if len(llist) > 0 :
        if answer == llist[0][0] :
            # 오른쪽 회전
            if llist[0][1] == "D" :
                d += 1
                if d > 3 :
                    d = 0
            # 왼쪽 회전
            elif llist[0][1] == "L" :
                d -= 1
                if d < 0 :
                    d = 3
            llist.popleft()

print(answer)