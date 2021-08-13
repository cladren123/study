import sys

"""
k를 분배해서 레벨업을 한다.

"""


input = sys.stdin.readline

n, k = map(int, input().split())

level = []

for _ in range(n) :
    level.append(int(input()))


# level 을 이분탐색 해야한다.

start = 1
end = 1000000000

while start <= end :
    mid = (start + end) // 2

    res = 0

    for i in level :
        if i > mid :
            continue
        else :
            res += mid - i

    if k >= res :
        start = mid + 1
        answer = mid
    else :
        end = mid - 1

print(end)
