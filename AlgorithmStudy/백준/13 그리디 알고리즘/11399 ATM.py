"""

문제 유형 : 그리디

돈을 인출하는데 필요한 시간의 합의 최솟값을 구하라

"""
import sys

input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))

# 최솟값이 될려면 가장 짧은 사람먼저 뽑아서 기다리는 시간을 최소화 해야 한다.

nl.sort()

count = 0
answer = 0

for i in nl :
    count += i
    answer += count

print(answer)

