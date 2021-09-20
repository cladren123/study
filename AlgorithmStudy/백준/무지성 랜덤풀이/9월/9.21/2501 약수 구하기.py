"""

문제유형 :
수학
브루트포스 알고리즘

"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

alist =[]

for i in range(1,n+1) :
    if n % i == 0 :
        alist.append(i)

an = len(alist)

answer = 0

if an < k :
    print(answer)
else :
    answer = alist[k-1]
    print(answer)

