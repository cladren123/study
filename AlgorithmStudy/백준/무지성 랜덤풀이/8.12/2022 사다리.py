import sys

input = sys.stdin.readline

x,y,c = map(int, input().split())


"""
c = 루트(x의 제곱 - ans의 제곱) - 루트(y의 제곱 - ans의 제곱)

start
end

모르겠다.. 시불...

"""

start = 0
end = min(x,y)

while start <= end :
    mid = (start + end) // 2

    ans = abs((x**2 - mid**2)**0.5 - (y**2 - mid**2)**0.5)

    if c >= ans :
        end = mid - 1

    else :
        start = mid + 1

print(end)

