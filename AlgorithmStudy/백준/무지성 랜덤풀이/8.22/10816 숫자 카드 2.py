"""

문제 유형 : 이분 탐색

시간초과 발생
answerlist = [0] * m

for i in range(m) :
    for j in range(n) :
        if mlist[i] == nlist[j] :
            answerlist[i] += 1

print(*answerlist)

딕셔너리도 공부해서 정리해야겠다.


"""
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

ndict = defaultdict(int)

for i in nlist :
    ndict[i] += 1

# print(ndict)

for i in mlist :
    print(ndict[i], end=" ")




