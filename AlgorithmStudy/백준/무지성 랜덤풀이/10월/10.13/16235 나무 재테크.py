
import sys

input = sys.stdin.readline



# 봄 : 양분 먹음, 양분 못 먹으면 죽음
# 여름 : 봄에 죽은 나무가 양분이 된다. 즉은 나무의 나이를 2로 나눈 값이 양분이 된다.
# 가을 : 나무 번식, 나무의 나이가 5의 배수, 인저반 8개의 칸에 나이가 1인 나무가 생긴다.
# 겨울 : 양분 추가. 양분의 양은 A[r][c]이다.

# k 년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하라.

# n : 땅의 크기, m : 나무의 개수, k : 년수
n, m, k = map(int, input().split())

# 처음 땅은 양분이 모두 5
ground = [[5] * (n+1) for _ in range(n+1)]



# a는 겨울에 공급된 양분의 양
a = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    one = list(map(int,input().split()))
    for j in range(1,n+1) :
        a[i][j] = one[j-1]



# # 나무 심기, 3차원
trees = [[[] for _ in range(n+1)] for _ in range(n+1)]


for _ in range(m) :
    y,x,ages = map(int, input().split())
    trees[y][x].append(ages)

def spring() :
    for y in range(1,n+1) :
        for x in range(1,n+1) :
            if len(trees[y][x]6566666666666666666)














