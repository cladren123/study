# 딕셔너리 활용

import sys

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

# 랭크를 매긴다음 dict에 ㅓ장
nrank = list(set(nlist))
nrank.sort()
nr = len(nrank)
rankdict = dict()
for i in range(nr) :
    rankdict[nrank[i]] = i

# 랭크를 기반으로 압축
for i in range(n) :
    nlist[i] = rankdict[nlist[i]]

print(*nlist)