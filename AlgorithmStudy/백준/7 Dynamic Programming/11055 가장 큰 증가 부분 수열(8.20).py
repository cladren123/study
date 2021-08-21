"""

문제 유형 = DP

DP를 초기값을 줄 때 기존의 리스트로 하자.

i번째의 dp를 구할 때
j를 이용해 i번째 보다 작은 것들을 찾는다.


"""
import copy
import sys


input = sys.stdin.readline


# n : 수열의 크기
n = int(input())

# 수열
nlist = list(map(int, input().split()))

# dp 생성과 초기값을 부여
dp = copy.deepcopy(nlist)


for i in range(n) :
    for j in range(i) :
        if nlist[i] > nlist[j] :
            dp[i] = max(dp[i], dp[j] + nlist[i])

# print(dp)
print(max(dp))












