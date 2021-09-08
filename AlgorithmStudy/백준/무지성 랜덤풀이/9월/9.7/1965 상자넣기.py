"""

문제 유형 : DP

"""
import sys

input = sys.stdin.readline

# 상자의 개수 입력
n = int(input())

# 상자의 크기 리스트 입력
nl = list(map(int, input().split()))

# DP 생성. 자신부터 세기 때문에 초기값을 1로 한다.
dp = [1] * n


# DP[i] : i번째 위치에서 상자가 최대 몇개 담길 수 있는가를 저장
for i in range(n) :

    # i번째 이전의 값들을 조사한다.
    # 조건이 충족되면 자기 자신에 +1 된 값중 가장 큰 값을 dp[i]에 저장한다.
    for j in range(i) :
        if nl[i] > nl[j] :
            dp[i] = max(dp[i], dp[j] + 1)

# 정답 출력
# print(dp)
print(max(dp))