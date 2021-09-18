"""

문제유형 :
브루트포스

"""
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())

nlist = []
for i in range(1,n+1) :
    nlist.append(i)

answer = list(permutations(nlist, n))

for i in answer :
    print(*i)
