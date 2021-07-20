import sys

input = sys.stdin.readline

# n 나무의 개수, m 가저가야할 나무
n, m = map(int, input().split())

trees = list(map(int, input().split()))

# print(n,m)
# print(trees)

# 높이에 최대값 설정

answer = 0

start = 0
end = max(trees)


while start <= end :
    allAdd = 0
    mid = (start + end) // 2

    for i in trees :
        if i >= mid :
            allAdd += i - mid

    if allAdd >= m :
        start = mid + 1
    else :
        end = mid - 1

print(end)



