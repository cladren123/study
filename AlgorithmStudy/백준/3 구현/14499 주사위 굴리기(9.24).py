"""

문제유형 :
구현
시뮬레이션

처음 주사위의 모든 면은 0 이다..

주사위 좌표가 세로, 가로 순으로 주어진다.
예시는 다 맞았는데 채점하자마자 틀리면 이것을 의심해보자.

"""
import sys

input = sys.stdin.readline
# n : 세로, m : 가로, y,x: 주사위 좌표(세로,가로), k : 명령 개수
n, m, y, x, k = map(int, input().split())
board = []
for _ in range(n) :
    one = list(map(int, input().split()))
    board.append(one)
order = list(map(int, input().split()))

dice = [0] * 7

# 0 동 서 북 남
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]


def move(direct) :
    global dice
    # 동쪽 1,3,4,6
    # 6 = 4, 3 = 6, 1 = 3, 4 = 1
    if direct == 1 :
        dice[6], dice[3], dice[1], dice[4] = dice[4], dice[6], dice[3], dice[1]
    # 서쪽
    # 6 = 3, 3 = 1, 1 = 4, 4 = 6
    elif direct == 2 :
        dice[6], dice[3], dice[1], dice[4] = dice[3], dice[1], dice[4], dice[6]
    # 북쪽
    # 6 = 5, 5 = 1, 1 = 2, 2 = 6
    elif direct == 3 :
        dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]
    #남쪽
    # 6 = 2, 5 = 6, 1 = 5, 2 = 1
    elif direct == 4 :
        dice[6], dice[5], dice[1], dice[2] = dice[2], dice[6], dice[5], dice[1]

# 명령 수행
for direct in order :
    ny = y + dy[direct]
    nx = x + dx[direct]

    # 이동한 방향이 범위에 들어오면 실행
    if 0 <= ny < n and 0 <= nx < m :
        # 주사위 굴리기
        move(direct)

        # 칸의 숫자가 없을 경우 주사위 바닥면이 칸에 복사
        if board[ny][nx] == 0 :
            board[ny][nx] = dice[1]
        # 칸의 숫자가 있을 경우 칸의 수가 주사위 바닥면에 복사, 칸의 수 0
        else :
            dice[1] = board[ny][nx]
            board[ny][nx] = 0

        # 윗면 출력하기
        print(dice[6])

        # 위치 이동하기
        y,x = ny,nx
























