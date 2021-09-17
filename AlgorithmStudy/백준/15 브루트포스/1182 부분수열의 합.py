"""

문제유형 :
브루트포스 알고리즘
백트랙킹

"""
import sys
from itertools import permutations, combinations

input = sys.stdin.readline

n, s = map(int, input().split())
nlist = list(map(int, input().split()))

answer = 0

for i in range(1, n+1) :
    a = list(combinations(nlist,i))

    for j in a :
        numbersum = 0

        for one in j :
            numbersum += one

        if s == numbersum :
            answer += 1



print(answer)