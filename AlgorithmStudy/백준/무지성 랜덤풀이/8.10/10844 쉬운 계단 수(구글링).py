
"""
https://pacific-ocean.tistory.com/151

각 자리수에서 맨 뒤에 올 수 있는 숫자의 개수로 점화식을 만든다.

           0  1  2  3  4  5  6  7  8  9
자리수(1)   0  1  1  1  1  1  1  1  1  1
자리수(2)   1  1  2  2  2  2  2  2  2  1
자리수(3)   1  3  3  4  4  4  4  4  3  2

해당 위치의 대각선 위의 숫자들의 합

예) 3이 뒷자리에 가려면, 앞은 2나 4가 나와야 한다.

0은 왼쪽 대각선이 없으므로 오른쪽 대각선
9는 오른쪽 대각선이 없으므로 왼쪽 대각선

i = 자리수
j = 맨 뒤에 갈 수 있는 경우의 수 (0~9)
"""


n = int(input())

dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)