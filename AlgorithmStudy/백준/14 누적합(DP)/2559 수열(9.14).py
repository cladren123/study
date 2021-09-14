
"""

문제 유형 :
누적합
두 포인터

연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램

"""
import sys

input = sys.stdin.readline


# n : 수의 개수  k : 합할 개수
n, k = map(int, input().split())
board = list(map(int, input().split()))

dp1 = [0] * (n+1)
dp1[1] = board[0]

for i in range(1,n+1) :
    dp1[i] = dp1[i-1] + board[i-1]

# print(dp1)

answer = -sys.maxsize

for i in range(k, n+1) :
    one = dp1[i] - dp1[i-k]
    # print(one)
    answer = max(answer, one)

print(answer)








