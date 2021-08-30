"""

문제 유형 : 그리디

서류, 면접이 모두 떨어지면 배제된다.

"""
import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :

    # 지원자의 숫자
    n = int(input())

    board = []

    for _ in range(n) :
        s,m = map(int, input().split())
        board.append([s,m])


    board.sort()

    # print(board)

    checker = board[0][1]

    answer = n

    for i in range(1,n) :
        if checker < board[i][1] :
            answer -= 1

        checker = min(checker, board[i][1])

    print(answer)










