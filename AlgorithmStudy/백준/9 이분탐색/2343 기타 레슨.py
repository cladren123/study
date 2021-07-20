import sys

input = sys.stdin.readline

n,m = map(int, input().split())

blist = list(map(int, input().split()))


# blist[-1]을 하면 58%을 넘지 못한다.
start = max(blist)
end = sum(blist)

while start <= end :
    mid = (start + end) // 2

    checksum = 0
    blueray = 0

    for i in blist :
        if (checksum + i)  > mid :
            blueray += 1
            checksum = 0
        checksum += i

    if checksum :
        blueray += 1

    if blueray <= m :
        end = mid - 1
    else :
        start = mid + 1


# print(start)
print(start)








