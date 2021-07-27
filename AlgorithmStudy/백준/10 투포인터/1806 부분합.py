import sys

input = sys.stdin.readline
n,s = map(int, input().split())
nlist = list(map(int, input().split()))

start = 0
end = 1
sumcount = 0

answer = sys.maxsize

while start < n and end < n :

    for i in range(start,end+1) :
        sumcount += nlist[i]

    if sumcount >= s :
        check = end - start + 1
        answer = min(check, answer)
        start += 1
        end = start
        if check == 2 :
            break
    sumcount = 0
    end += 1

print(answer)









