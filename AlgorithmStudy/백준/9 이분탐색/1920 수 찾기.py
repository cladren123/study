import sys

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

answer = [0] * m

def find(nindex, target, nlist) :
    global answer
    global n
    left = 0
    right = n - 1

    while left <= right :
        mid = (left + right) // 2
        if nlist[mid] == target :
            answer[nindex] = 1
            break
        elif nlist[mid] > target :
            right = mid - 1
        else :
            left = mid + 1

for i in range(m) :
    find(i, mlist[i], nlist)

for j in answer :
    print(j)


