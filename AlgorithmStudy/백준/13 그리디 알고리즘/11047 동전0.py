"""

문제 유형 : 그리디

동전 개수를 최솟값으로 해서 모든 가치의 합을 K로 만들기

"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

worth = []

for _ in range(n) :
    worth.append(int(input()))

# print(worth)

worth.sort(reverse=True)

answer = 0

for i in worth :
    answer += k // i
    k = k % i
    if k == 0 :
        break

print(answer)

