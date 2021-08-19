"""
4 + 4 + 3+ 2 = 13

"""
import sys

input = sys.stdin.readline

# n : 필요한 랜선의 개수
# k : 이미 가지고 있는 랜선의 개수

k, n = map(int, input().split())

linelist = []

for i in range(k) :
    one = int(input())
    linelist.append(one)


start = 1
# max 값을 그냥 무시하고 제일 큰 값을 정해야 한다.
end = max(linelist)

while start <= end  :
    mid = (start + end) // 2
    # print(mid)

    allsum = 0

    for i in linelist :
        sumone = i // mid
        allsum += sumone

    # print("allsum : %d mid : %d" %(allsum ,mid))
    # print("start : %d end : %d" %(start, end))

    # allsum 잘린 랜선의 수
    if allsum >= n :
        start = mid + 1
    else :
        end = mid - 1

print(end)





