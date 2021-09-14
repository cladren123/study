
"""

문제유형 :
누적합
스위핑
두 포인터
슬라이딩 윈도우

"""
import sys

input = sys.stdin.readline

# n : 신호등의 개수 k : 연속된 신호등의 수 b : 고장난 신호등 수
n, k, b = map(int, input().split())

board = [0] * (n+1)


for _ in range(b) :
    one = int(input())
    board[one] = 1


# print(board)

chogi = 0

for i in range(1,k+1) :
    chogi += board[i]

# print(chogi)
answer = []
answer.append(chogi)

for i in range(k+1, n+1) :
    if board[i] == 1 :
        chogi += 1
    if board[i-k] == 1 :
        chogi -= 1

    answer.append(chogi)

# print(answer)
print(min(answer))





