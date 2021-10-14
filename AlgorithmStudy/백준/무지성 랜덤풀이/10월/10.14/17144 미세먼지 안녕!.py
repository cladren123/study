
import sys
import copy

input = sys.stdin.readline

# r : 세로, c : 가로, t : 시간
r, c, t = map(int, input().split())

a = []

for _ in range(r) :
    one = list(map(int, input().split()))
    a.append(one)

# 공기 청정기 위치 탐색
aircleaner = []
for y in range(r) :
    for x in range(c) :
        if a[y][x] == -1 :
            aircleaner.append([y,x])

y1, x1 = aircleaner[0][0], aircleaner[0][1]
y2, x2 = aircleaner[1][0], aircleaner[1][1]

# 확산
def diffusion() :
    global a
    newa = copy.deepcopy(a)

    newa[y1][x1] = -1
    newa[y2][x2] = -1

    # 네 방향
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    for y in range(r) :
        for x in range(c) :
            # 확산 대상 미세먼지
            if a[y][x] > 4 :
                # 확산 방향 탐지
                hubo = []
                for d in range(4) :
                    ny = y + dy[d]
                    nx = x + dx[d]
                    # 확산 대상은 범위 안에 있고 공기청정기가 아니다
                    if 0 <= ny < r and 0 <= nx < c and a[ny][nx] != -1 :
                        hubo.append([ny,nx])


                for one in hubo :
                    newa[one[0]][one[1]] += (a[y][x] // 5)

                newa[y][x] = newa[y][x] - (a[y][x]//5)*len(hubo)

    a = copy.deepcopy(newa)


# 공기청정기 가동
# 공기청정기는 항상 1열에 설치되어 있다.
def air() :
    global a
    newa = [[0] * c for _ in range(r)]



    # 위쪽 지역
    for y in range(y1+1) :
        for x in range(c) :
            # 먼지일 때 움직인다.
            if a[y][x] >= 1 :
                # 천장이면 왼쪽으로 이동
                if y == 0 and x-1 >= 0 :
                    newa[y][x-1] = a[y][x]
                # 오른쪽 벽이면 위로 이동
                elif x == (c-1) and y >= 0 :
                    newa[y-1][x] = a[y][x]
                # 왼쪽 벽이면 아래로 이동
                elif x == 0 :
                    newa[y+1][x] = a[y][x]
                # 아래쪽은 오른쪽으로 이동
                elif y == y1 and x+1 < c :
                    newa[y][x+1] = a[y][x]
                # 나머지는 그대로
                else :
                    newa[y][x] = a[y][x]



    #아래쪽 지역
    for y in range(y1+1,r) :
        for x in range(c) :
            # 먼지 일 때 이동
            if a[y][x] >= 1 :
                # 위쪽 천장 오른쪽 이동
                if y == y1+1 and x+1 < c :
                    newa[y][x+1] = a[y][x]
                # 오른쪽 벽 아래 이동
                elif x == c-1 and y+1 < r :
                    newa[y+1][x] = a[y][x]
                # 왼쪽 벽 위로 이동. 공기청정기를 만나면 소멸
                elif x == 0  :
                   newa[y-1][x] = a[y][x]
                # 아래쪽은 왼쪽으로 이동
                elif y == r-1 and x-1 >= 0 :
                    newa[y][x-1] = a[y][x]
                # 나머지는 그대로
                else :
                    newa[y][x] = a[y][x]

    newa[y1][x1] = -1
    newa[y2][x2] = -1

    a = copy.deepcopy(newa)

    # 미세먼지의 양 측정
    result = 0
    for y in range(r) :
        for x in range(c) :
            if a[y][x] >= 1 :
                result += a[y][x]

    return result



for _ in range(t) :
    diffusion()
    answer = air()



print(answer)








