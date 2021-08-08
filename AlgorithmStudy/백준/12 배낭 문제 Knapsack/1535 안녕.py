"""
난이도 : 실버2

"""
import sys

input = sys.stdin.readline

# n : 사람 수
n = int(input())

# 체력을 잃는 값을 담은 리스트
lost = [0] + list(map(int, input().split()))

# 행복값을 담은 리스트
happy = [0] + list(map(int, input().split()))


# dp 리스트, 세로는 사람의 개수, 가로는 체력 100이 되면 죽으니 99까지 담아야 한다.
dp = [[0] * (101) for _ in range(n+1)]


for i in range(1,n+1) :
    # 정렬을 안했기 때문에 처음했던 range(i,100)을 쓰면 오답으로 나온다.
    for j in range(100) :

        # 사람마다 체력 잃는 값과 행복값을 뽑는다.
        loose = lost[i]
        hap = happy[i]

        # 체력값이 손실값보다 작으면 이전의 dp의 값을 받는다.
        if j < loose :
            dp[i][j] = dp[i-1][j]

        # 체력값이 손실값보다 클 때
        # 현재의 행복값을 더하고 남은 체력에 해당하는 행복값을 더한 것과
        # 이전의 체력값을 비교해서 더 큰 값을 dp 에 넣는다.
        else :
            dp[i][j] = max(hap + dp[i-1][j-loose], dp[i-1][j])


# for i in dp :
#     print(i)


# 마지막에는 가장 큰 행복값이 담긴다.
print(dp[n][99])






