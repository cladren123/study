"""


"""

n, c = map(int, input().split())

house = []
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 거리의 최솟값과 최대값
start = 1
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start + end) // 2  # 해당 gap
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:  # gap 이상
            count += 1
            old = house[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)