# 구글링, 다시 한 번 풀어보자

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nlist = []

for _ in range(n) :
    nlist.append(int(input()))

# print(n,m)
# print(nlist)

nlist.sort()

# answer = 20000000001
answer = sys.maxsize

p1 = 0
p2 = 1

while p1 < n and p2 < n  :
    check = nlist[p2] - nlist[p1]
    if check == m :
        answer = check
        break
    if check < m :
        p2 += 1
        continue
    p1 += 1
    answer = min(answer, check)


print(answer)



