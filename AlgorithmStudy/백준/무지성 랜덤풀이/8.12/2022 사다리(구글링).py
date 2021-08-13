

"""
w1:c = w:h2
w2:c = w:h1

이 식을 풀면

c = h1*h2(h1+h2) 높이




공식 에바야...


"""
import sys

input = sys.stdin.readline


x,y,c = map(float, input().split())

start = 0
end = min(x,y)

res = 0

while end-start > 0.000001 :
    mid = (start + end) / 2

    h1 = (x**2 - mid**2) ** 0.5
    h2 = (y**2 - mid**2) ** 0.5

    c1 = h1 * h2 / (h1+h2)

    if c1 >= c :
        res =mid
        start = mid
    else :
        end = mid


print("%0.3f" %res)















