"""

문제 유형 : 이분탐색

n 개 중 1개, 2개, 3개를 뽑아 C가 되는지 확인하는 문제


시간초과
# 하나 비교
for i in range(n) :
    if c == w[i] :
        answer = 1
if n >= 2 :
    w2 = list(combinations(w, 2))
    for i1, i2 in w2 :
        if c == (i1 + i2) :
            answer = 1

if n >= 3 :
    w3 = list(combinations(w,3))
    for i1,i2,i3 in w3 :
        if c == (i1+i2+i3) :
            answer = 1

print(answer)

"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, c = map(int, input().split())
w = list(map(int, input().split()))

answer = 0

w.sort()

check = [0] * 100000001

for i in w :
    check[i] = 1


if check[c] == 1 :
    answer = 1
else :
    for i in range(n-1) :
        for j in range(i+1, n) :

            if w[i] + w[j] == c :
                answer = 1
                break

            if w[i] + w[j] <= c :
                diff = c - w[i] - w[j]
                if check[diff] == 1 and diff != w[i] and diff != w[j]:
                    answer = 1
                    break


print(answer)




