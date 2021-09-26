"""

문제유형 :
그래프 이론
그래프 탐색
브루트포스 알고리즘
너비 우선 탐색

"""
import copy
import sys
from collections import deque

input = sys.stdin.readline

# 승원이는 m개를 활성 상태로 변경한다.
# 0 빈칸, 1 벽, 2 바이러스
# 모든 칸에 바이러스를 퍼뜨리는 최소 시간을 구한다.

# n : 연구소의 크기, m : 바이러스 개수
n, m = map(int, input().split())

board = []

for i in range(n) :
    board.append(list(map(int, input().split())))

# 2의 개수와 위치를 선별하자.
virus = []

for i in range(n) :
    for j in range(n) :
        if board[i][j] == 2 :
            virus.append([i,j])

# 바이러스의 개수
vnum = len(virus)
visited = [0] * vnum

# 4방향을 탐색
dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 바이러스가 몇초안에 뒤덮는지 구하는 함수
# bfs를 통해 구하자
# 비활성바이러스를 만나면 시간은 그대로. 하지만 비활성 바이러스를 퍼뜨릴때는 +1 해야한다. 헷갈린다.
def spread(svirus) :
    que = deque()
    global board

    # board를 복사하고 빈 공간을 -1로 만든다.
    newboard = copy.deepcopy(board)
    for i in range(n) :
        for j in range(n) :
            # 빈 땅을 -1로 치환
            if newboard[i][j] == 0 :
                newboard[i][j] = -1
            # 벽을 -10으로 치환
            if newboard[i][j] == 1 :
                newboard[i][j] = -10

    # 재방문을 방지하기 위한 2차원 리스트
    boardvisited = [[0] * n for _ in range(n)]

    for y,x in svirus :
        boardvisited[y][x] = 0
        newboard[y][x] = 0
        newone = [y,x,0,0,0]
        que.append(newone)

    # 바이러스를 퍼트리는 과정
    while que :
        # vflag는 비활성 바이러스를 만났다는 표시
        y,x,time,vflag,sv = que.popleft()


        for direct in range(4) :
            ny = y + dy[direct]
            nx = x + dx[direct]

            if 0 <= ny < n and 0 <= nx < n :
                # 방문한 적이 없고 벽이 아니면 탐색
                if boardvisited[ny][nx] == 0 and newboard[ny][nx] != -10 :
                    # 비활성바이러스 -> 빈공간일 경우 비활성바이러스 수를 더한다
                    if newboard[ny][nx] == -1 and vflag == 1:
                        boardvisited[ny][nx] = 1
                        newboard[ny][nx] = sv+1+time
                        que.append([ny,nx,sv+1+time,0,0])
                    # 바이러스 -> 비활성바이러스 : 시간 정지
                    elif newboard[ny][nx] == 2 and vflag == 0 :
                        boardvisited[ny][nx] = 1
                        newboard[ny][nx] = time
                        que.append([ny,nx,time,1,sv+1])
                    # 비활성바이러스 -> 비활성바이러스 일 경우 시간 0
                    elif newboard[ny][nx] == 2 and vflag == 1 :
                        boardvisited[ny][nx] = 1
                        newboard[ny][nx] = time
                        que.append([ny,nx,time,1,sv+1])
                    # 바이러스 -> 빈공간일 경우 +1
                    elif newboard[ny][nx] == -1 and vflag == 0:
                        boardvisited[ny][nx] = 1
                        newboard[ny][nx] = time + 1
                        que.append([ny, nx, time + 1, 0, 0])



    # 바이러스를 퍼뜨리는데 걸린 시간
    result = 0
    zflag = 0
    for i in newboard :
        result = max(result, max(i))
        if -1 in i :
            zflag = 1

    # if result == 3 :
    #     print(svirus)
    #     for i in newboard :
    #         print(i)
    #     print()



    if zflag == 1 :
        result = -1

    return result

answer = set()
# 활성화 바이러스 선택 : 전체 바이러스 중 m개를 선택한다.
def dfs(stage, idx, select) :
    global answer
    # 종단조건, 바이러스가 퍼지는데 가장 작게 걸린 경우를 답으로 출력
    if stage == m :
        answer.add(spread(select))
        return


    # 바이러스 탐색
    for i in range(idx, vnum) :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(stage+1, i, select + [virus[i]])
            visited[i] = 0


dfs(0,0,[])
# print(answer)
if len(answer) >= 2 :
    if -1 in answer :
        answer.remove(-1)

print(min(answer))





