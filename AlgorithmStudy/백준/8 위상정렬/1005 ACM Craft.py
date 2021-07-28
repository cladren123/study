import sys
from collections import deque

input = sys.stdin.readline

# n 건물의 개수, k 건설순서규칙
n, k = map(int, input().split())

nlist = [[]  for _ in range(n+1)]


ntime = list(map(int, input().split()))


for _ in range(k) :
    s, e = map(int, input().split())
    nlist[e].append(s)

w = int(input())

print(nlist)


que = deque()














