

"""

문제 유형 : DP

    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
12  0 0 0 0 0 0 0 0 0  0  0  1  0  0  0
5   0 0 0 0 1 0 0 0 0  2  0  1  0  0  3
1   1 2 3 4 1 2 3 4 5  2  3  1  2  3  3

"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = []

for _ in range(n) :
    coin.append(int(input()))

# coin 리스트에 중복과정 제거
coin = set(coin)
coin = list(coin)

coin.sort(reverse=True)

n = len(coin)

answer = -1

# dp 생성
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,k+1) :
        cur = coin[i-1]

        # 코인이 맞아 떨어지면 +1
        if j % cur == 0 :
            dp[i][j] = dp[i][j-cur] + 1

        # 이전의 coin과 현재의 coin이 더해저서 맞아떨어지면 +1
        if j-cur >= 0 and dp[i][j-cur] != 0 :
            dp[i][j] = dp[i][j-cur] + 1

        # 이전의 값과 현재의 값을 비교해서 더 작은 값을 dp에 저장한다.
        if dp[i-1][j] != 0 :
            if dp[i][j] == 0 :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = min(dp[i-1][j], dp[i][j])








# for i in dp :
#     print(i)

# 최종적으로 나온 값이 나누어떨어지지 않으면 0이 되므로
# 0이면 -1을 출력 그렇지 않으면 정답을 출력
if dp[n][k] != 0 :
    answer = dp[n][k]

print(answer)

"""

나누어 떨어지는 경우와 더해서 떨어지는 경우
2개를 모두 고려해야 한다. 

"""

















