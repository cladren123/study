"""


"""
import sys

input = sys.stdin.readline

# n : 필요한 랜선의 개수
# k : 이미 가지고 있는 랜선의 개수

n, k = map(int, input().split())

linelist = []

for i in range(n) :
    one = int(input())
    linelist.append(one)


start = 1
end = min(linelist)

while start <= end :
    mid = (start + end) // 2
    # print(mid)

    allsum = 0

    for i in linelist :
        sumone = i // mid
        allsum += sumone

    # print("allsum : %d" %allsum)

    # allsum 잘린 랜선의 수
    if allsum >= k :
        start = mid + 1
    else :
        end = mid - 1

print(end)





