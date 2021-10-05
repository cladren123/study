"""

문제유형 :
문자열
정렬

"""

import sys

input = sys.stdin.readline

n = input().strip()

n = list(n)
n.sort(reverse=True)

for i in n :
    print(i, end = "")