"""

문제유형 :
구현
브루트포스
시뮬레이션

시시티비를 4가지 방향으로 돌려 모든 경우의 수에 사각 지대를 구한다.
그 중 사각 지대의 최소 크기를 출력한다.

1 : 한 방향 4
2 : 앞, 뒤 2
3 : 앞 90도 4
4 : 3 방향 4
5 : 모든 방향 1

중복이 가능한 모든 경우의 수를 구해야 한다.
중복순열 product를 활용한다.

구글링 결과 방향을 함수로 미리 만들어둔다.

모듈화를 잘 하냐가 관점

"""
import sys

input = sys.stdin.readline

# n 세로 m 가로
n,m = map(int, input().split())
board = []

for _ in range(n) :
    board.append(list(map(int, input().split())))

# 동, 남, 서, 북
dx = [1,0,-1,0]
dy = [0,-1,0,1]

direct = [
    [],
    [1,2,3,4],
    [[1,3], [2,4]],
    [[1,2], [2,3], [3,4], [4,1]],
    [[1,2,3], [2,3,4], [3,4,1], [4,1,2]],
    [[1,2,3,4]]
]









