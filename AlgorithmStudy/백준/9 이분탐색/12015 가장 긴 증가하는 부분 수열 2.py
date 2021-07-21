import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

start = 0
end = n

while start <= end :
    mid = (start+end)//2


    count = 0

    for i in range(n) :
        check = a[i]
        for j in range(i,n) :
            if check < a[j] :
                check = a[j]
                count += 1
        if count >= mid :











