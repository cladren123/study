"""
설명은 좋은데 틀림..
https://kangmin1012.tistory.com/34

정답
https://infinitt.tistory.com/247

"""


import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1) :
    # 1을 뺏을 경우 나오는 경우의 수를 저장
    dp[i] = dp[i-1] + 1
    
    # 2로 나누어질 경우 기존 1을 뺏을 경우의 수와 비교하여 최소값 저장
    if i%2 == 0  :
        dp[i] = min(dp[i], dp[i//2] + 1)

    # 3으로 나누어질 경우 기존 1을 뺏을 경우의 수와 비교하여 최소값 저장
    # 여기서는 2또는 3으로 나누어질 경우 모든 경우를 봐야하므로 elif 가 아닌 if로 설정
    if i%3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])