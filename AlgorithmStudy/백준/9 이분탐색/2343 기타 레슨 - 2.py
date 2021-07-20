import sys

input = sys.stdin.readline

n, m = map(int, input().split())

blist = list(map(int, input().split()))

start = max(blist)
end = sum(blist)

while start <= end:
    mid = (start + end) // 2

    checksum = 0
    blueray = 0

    for i in blist:
        if (checksum + i) > mid:
            blueray += 1
            checksum = 0
        checksum += i

    if checksum:
        blueray += 1

    if blueray > m:
        start = mid + 1
    else:
        end = mid - 1

# print(start)
print(start)








