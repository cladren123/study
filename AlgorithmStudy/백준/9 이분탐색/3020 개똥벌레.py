import sys

input = sys.stdin.readline

# N 장애물의 개수, H 동굴의 높이
# 2 <= N <= 200000, for문 두 번 쓰면 안되겠는데..
N,H = map(int, input().split())

ob = []

for _ in range(N) :
    ob.append(int(input()))

print(ob)

# 파괴해야 하는 장애물의 최솟값

start = 1
end = N

sama = N
answerlist = []

while start <= end :
    mid = (start + end) // 2

    count = 0

    for i in range(0,N,2) :
        if 0 <= mid <= ob[i] :
            count += 1
    for j in range(1,N,2) :
        if H - ob[j] <= mid <= H :
            count += 1

    answerlist.append(count)

print(count)













