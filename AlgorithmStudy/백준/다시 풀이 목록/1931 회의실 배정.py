"""

문제 유형 : 그리디

정해저 있는 시간표들을 잘 배치해 최대한 많은 시간표를 만들기.

이를 위해서 끝나는 시간이 중요하다. 일찍 끝나야 그 뒤에 많은 시간이 올 수 있다.

끝나는 시간으로 정렬한다. 그 다음 끝나는 시간 다음으로 빨리 시작하는게 와야 한다.

시작 시간을 기준으로 정렬한다.

count를 세면 된다.


"""
import sys

input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n) :
    start, end = map(int, input().split())

    board.append([start, end])

# 이중 정렬 : x[1]을 기준으로 먼저 정렬하고 x[0]을 기준으로 정렬한다.
board.sort(key=lambda x : (x[1], x[0]))

# print(board)

answer = 0

bend = 0

for i in board :
    start = i[0]
    end = i[1]

    if bend <= start :
        answer += 1
        bend = end

print(answer)










