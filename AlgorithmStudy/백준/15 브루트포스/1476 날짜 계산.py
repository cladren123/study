"""

문제유형 :
수학
구현
브루트포스 알고리즘
정수론
중국인의 나머지 정리

"""
import sys

input = sys.stdin.readline

e,s,m = map(int, input().split())

# 1 <= e <= 15
# 1 <= s <= 28
# 1 <= m <= 19

year = 0
earth = 0
sun = 0
moon = 0

while True :
    year += 1
    earth += 1
    sun += 1
    moon += 1

    if earth > 15 :
        earth -= 15
    if sun > 28 :
        sun -= 28
    if moon > 19 :
        moon -= 19

    if earth == e and sun == s and moon == m :
        print(year)
        break















