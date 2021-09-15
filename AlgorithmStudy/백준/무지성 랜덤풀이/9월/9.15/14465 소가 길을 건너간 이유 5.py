
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

# 고장난 신호등의 정보를 담을 배열
board = [0] * (n+1)

# 고장난 신호등은 1로 표시
for _ in range(b) :
    one = int(input())
    board[one] = 1

# 고장난 신호등을 담을 변후
breaksignal = 0

# 1부터 k번까지 고장난 신호등의 개수를 파악
for i in range(1,k+1) :
    breaksignal += board[i]

# 구간 별 고장난 신호등의 개수를 담을 리스트
answer = []
answer.append(breaksignal)

# 1칸씩 이동하면서 범위에서 고장난 신호등이 벗어나면 -1, 포함되면 +1을 한다.
for i in range(k+1, n+1) :
    if board[i] == 1 :
        breaksignal += 1
    if board[i-k] == 1 :
        breaksignal -= 1

    answer.append(breaksignal)

# 정답리스트의 최소값이 정답이 된다.
print(min(answer))





