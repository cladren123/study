
"""
이분탐색

1. 최소값, 최대값을 구한다
2. while 문을 이용한 이분탐색

"""


import sys

input = sys.stdin.readline


n, c = map(int, input().split())

house = []

for _ in range(n) :
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]

while (start <= end) :
    mid = (start + end) // 2
    old = house[0]
    count = 1

    for i in range(1, len(house)) :
        if house[i] >= old + mid :
            count += 1
            old = house[i]


    # 이상인 곳이 답이 되는 곳 이다.
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1




print(result)










