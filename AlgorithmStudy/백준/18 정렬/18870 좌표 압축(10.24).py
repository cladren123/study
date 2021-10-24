# 딕셔너리 활용

import sys

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

nrank = list(set(nlist))
nrank.sort()

nr = len(nrank)

rankdict = dict()

for i in range(nr) :
    rankdict[nrank[i]] = i

for i in range(n) :
    nlist[i] = rankdict[nlist[i]]

print(*nlist)

















