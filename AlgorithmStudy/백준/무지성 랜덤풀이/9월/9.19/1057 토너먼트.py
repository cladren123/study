"""

문제유형 :
수학
브루트포스

1
1 3
1 2 3 4

두 수를 2로 나눈 몫을 서로 같아질때까지 빼다보면 라운드 수가 나온다.

"""
import sys

input = sys.stdin.readline
n, p1, p2 = map(int, input().split())

count = 0

while p1 != p2 :
    p1 -= p1//2
    p2 -= p2//2
    count += 1

print(count)





