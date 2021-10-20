

import sys


input = sys.stdin.readline;

# n : 단어의 개수
n = int(input());

nlist = []

for _ in range(n) :
    one = input().strip();
    nlist.append(one);

# 중복제거
nlist = set(nlist)
nlist = list(nlist)

nlist.sort();

ndict = dict();

for i in nlist :
    ni = len(i);
    if ni in ndict :
        ndict[ni].append(i);
    else :
        ndict[ni] = [i];


ndict = sorted(ndict.items())

for key,value in ndict :
    value.sort()
    for i in value :
        print(i)





