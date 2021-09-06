"""

문제 유형 : DP

3XN

2X1, 1X2

3을 채우려면
2X1 + 1X2
1X2 * 3

특수케이스 2개가 발생

"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (31)

dp[0] = 1
dp[2] = 3

# 짝수만 존재한다. 홀수는 모두 0 이다.

for i in range(4,n+1) :
    # 2X3 도형을 가장 오른쪽에 두는 경우, 2X3 도형이 3개이기 때문에 *3을 해준다.
    dp[i] = dp[i-2] * 3

    # n=4 부터 새로운 도형이 추가된다. 하지만 n이 4,6,8,10.. 일 때 도형의 모양이 모두
    # 다르기 때문에 각각 dp[i]에 더해준다.
    for j in range(4,i+1,2) :
        dp[i] += dp[i-j] * 2


print(dp[n])



