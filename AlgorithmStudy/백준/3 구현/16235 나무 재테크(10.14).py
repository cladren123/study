
import sys

input = sys.stdin.readline



# 봄 : 양분 먹음, 양분 못 먹으면 죽음
# 여름 : 봄에 죽은 나무가 양분이 된다. 즉은 나무의 나이를 2로 나눈 값이 양분이 된다.
# 가을 : 나무 번식, 나무의 나이가 5의 배수, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
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



# 나무 심기, 3차원
trees = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m) :
    y,x,ages = map(int, input().split())
    trees[y][x].append(ages)

# 죽은 나무 저장
dtrees = [[[] for _ in range(n+1)] for _ in range(n+1)]


def spring() :
    for y in range(1,n+1) :
        for x in range(1,n+1) :
            if len(trees[y][x]) >= 1 :
                count = 0
                for i in range(len(trees[y][x])) :
                    if ground[y][x] < trees[y][x][i] :
                        dtrees[y][x].append(trees[y][x][i])
                        count += 1
                    else :
                        ground[y][x] = ground[y][x] - trees[y][x][i]
                        trees[y][x][i] += 1
                # remove를 사용하면 원하지 않는 값이 삭제될 수 있다. 시작하자마자 틀렸다고 뜸
                for _ in range(count) :
                    trees[y][x].pop()

def summer() :
    for y in range(1,n+1) :
        for x in range(1,n+1) :
            if len(dtrees[y][x]) >= 1 :
                for one in dtrees[y][x] :
                    ground[y][x] += one//2
                dtrees[y][x].clear()


# 가을 : 나무 번식, 나무의 나이가 5의 배수일 때 인접한 8개 칸에 1살인 나무가 생긴다.
def fall() :
    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,-1,-1,-1,0,1,1,1]

    for y in range(1,n+1) :
        for x in range(1,n+1) :
            if len(trees[y][x]) >= 1 :
                for one in trees[y][x] :
                    if one % 5 == 0 :
                        for d in range(8) :
                            ny = y + dy[d]
                            nx = x + dx[d]

                            if 1 <= ny < n+1 and 1 <= nx < n+1 :
                                trees[ny][nx].insert(0,1)

# 기계가 돌아다니면서 양분을 준다.
def winter() :
    for y in range(1,n+1) :
        for x in range(1,n+1) :
            ground[y][x] += a[y][x]


for _ in range(k) :
    spring()
    summer()
    fall()
    winter()

answer = 0
for y in range(1,n+1) :
    for x in range(1,n+1) :
        answer += len(trees[y][x])

print(answer)