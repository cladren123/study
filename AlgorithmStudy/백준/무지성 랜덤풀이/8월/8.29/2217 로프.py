"""

문제 유형 : 그리디

가장 작은 거 * 갯수


"""
import sys

input = sys.stdin.readline

n = int(input())

lope = []

for _ in range(n) :
    lope.append(int(input()))

answer = 0

lope.sort()

for i in range(n) :
    answer = max(answer, lope[i] * (n-i))

print(answer)

