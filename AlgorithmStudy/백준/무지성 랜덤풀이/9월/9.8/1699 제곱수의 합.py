"""

문제 유형 : DP

1,4,9.19,16,25

26 루트 5.1

7 루트 2.6

answer = 0
while n >= 1 :
    sq = sqrt(n)
    sq = int(sq)
    n = n - sq**2
    answer += 1
print(answer)

DP를 활용해보자

"""
import sys

input = sys.stdin.readline

# 자연수 n 입력
n = int(input())

# 리스트를 n의 자리까지 만들기 위해 n+1 크기의 리스트 생성
dp = [i for i in range(n+1)]


for i in range(1, n+1) :
    for j in range(1,i) :
        # 탐색할 제곱수가 i보다 크면 더 이상 탐색이 불필요하기 때문에 중단한다.
        if j*j > i :
            break
        # 제곱수를 뺐을 때 조건을 만족하면 해당 위치에 +1 한 값으로 교체한다.
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1

print(dp[n])





