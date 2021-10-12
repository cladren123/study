

import sys

input = sys.stdin.readline


n = int(input())

nlist = []

for _ in range(n) :
    one = int(input())
    nlist.append(one)

nsum = sum(nlist)

# 산술평균
answer1 = round(nsum / n)
print(answer1)

nlist.sort()

# 중앙값
answer2 = nlist[n//2]
print(answer2)

# 최빈값
ndict = dict()

for i in nlist :
    if i in ndict :
        ndict[i] += 1
    else :
        ndict[i] = 1

# 최대값 구하기
mcount = max(ndict.values())


alist = []

for i in ndict :
    if mcount == ndict.get(i) :
        alist.append(i)

if len(alist) == 1 :
    print(alist[0])
else :
    print(alist[1])

# 범위 구하기
print(max(nlist) - min(nlist))



