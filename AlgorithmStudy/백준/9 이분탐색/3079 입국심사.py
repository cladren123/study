import sys

input = sys.stdin.readline

n,m = map(int, input().split())

testlist = []

for _ in range(n) :
    testone = int(input())
    testlist.append(testone)

start = 1
end = max(testlist) * m

while start <= end :
    count = 0
    mid = (start + end) // 2

    for i in testlist :
        count += mid//i

    # if count < m :
    #     start = mid + 1
    # else :
    #     end = mid - 1

    if count >= m :
        end = mid - 1
    else :
        start = mid + 1



# print(end)
print(start)



