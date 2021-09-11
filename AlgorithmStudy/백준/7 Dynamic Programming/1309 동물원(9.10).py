

"""

문제 유형 : DP

2XN

가로, 세로 붙어있게 배치할 수 없다.

N = 1  -> 3
0 0 / 1 0 / 0 1

1 2

N = 2 -> 7

0 0 / 0 0 / 0 0
0 0 / 1 0 / 0 1

1 0 / 1 0
0 0 / 0 1

0 1 / 0 1
0 0 / 1 0

3 4

3 4

N = 3
0 0 1 0 0 1
0 0 0 1
0 0 1 0

0 0 1 0 0 1
0 0 1 0

0 0 1 0 0 1
0 0 0 1

1 2
3 4
7 10
17 24

1이 하나로도 있는 것 : 0 * 2 + 1 * 1
1이 하나로도 없는 것 : 0 + 1






"""
import sys

input = sys.stdin.readline

# n 입력
n = int(input())

# 조건에 따라 나눌 값을 변수로 선언
number = 9901

# dp리스트 생성
dp = [[0] * 2 for _ in range(100001)]

# 초기값 생성
dp[1][0] = 1
dp[1][1] = 2

# 점화식 구현
if n > 1 :
    for i in range(2,n+1) :
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % number
        dp[i][1] = ((dp[i-1][0] * 2) + dp[i-1][1]) % number

# 정답 출력
answer = (dp[n][0] + dp[n][1]) % number
print(answer)






