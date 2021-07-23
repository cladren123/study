import sys

input = sys.stdin.readline

n1, n2 = map(int, input().split())

nlist1 = list(map(int, input().split()))
nlist2 = list(map(int, input().split()))

p1 = 0
p2 = 0
answer = []

while p1 < n1 and p2 < n2 :
    if nlist1[p1] < nlist2[p2] :
        answer.append(nlist1[p1])
        p1 += 1
    else :
        answer.append(nlist2[p2])
        p2 += 1

for i in range(p1,n1) :
    answer.append(nlist1[i])

for j in range(p2, n2) :
    answer.append(nlist2[j])

for k in answer :
    print(k, end = " ")



