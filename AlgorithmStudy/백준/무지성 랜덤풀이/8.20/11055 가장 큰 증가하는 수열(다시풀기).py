"""

문제 풀이

dp 각 자릿수에 가장 큰 값이 오게 하려면
dp[i] 보다 작은 인덱스들을 찾아 더해주면 된다.

테스트케이스 참고 사이트
https://joey09.tistory.com/108


"""
import sys

input = sys.stdin.readline


# n : 수열의 크기
n = int(input())

# 수열
nlist = list(map(int, input().split()))

dp = [x for x in nlist]
# dp = [0] * n
# print(dp)

dp[0] = nlist[0]

for i in range(n) :
    for j in range(i) :
        if nlist[i] > nlist[j] :
            dp[i] = max(dp[i], dp[j] + nlist[i])

# print(dp)
print(max(dp))