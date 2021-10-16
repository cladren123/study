

import sys

input = sys.stdin.readline

n = int(input())

nlist = [0] * 10001

for _ in range(n) :
    nlist[int(input())] += 1

for i in range(1,10001) :
    if nlist[i] >= 1 :
        for _ in range(nlist[i]) :
            print(i)







"""
메모리 초과 발생 
nlist.sort()
for i in nlist :
    print(i)
"""


