"""
실버2
틀렸습니다... ㅠㅠ

visited를 안써서 그런듯?

a,b,n,m = map(int, input().split())
# a,b,n,m = 2,3,1,20
que = deque()
checker = 0
que.append([n,0])
check = 0

while que :
    next,cur = que.popleft()


    caselist = [0] * 6
    caselist[0] = next + a
    caselist[1] = next * a
    caselist[2] = next + b
    caselist[3] = next * b
    caselist[4] = next + 1
    caselist[5] = next - 1

    caselist1 = set(caselist)
    caselist2 = list(caselist1)

    for j in caselist2 :
        if j > m :
            continue
        if j == m :
            print(cur+1)
            check = 1
            break
        else :
            que.append([j, cur + 1])

    if check == 1 :
        break
"""


from collections import deque

a,b,n,m = map(int, input().split())

# 돌다리
board = [0 for i in range(100001)]

# 방문체크
visited = [0] * 100001

dx = [-1,1,-a,a,-b,b,a,b]

que = deque()

que.append(n)
visited[n] = 1

while que :
    x = que.popleft()

    for i in range(8) :
        if i < 6 :
            nx = x + dx[i]

            if 0 <= nx < 100001 and visited[nx] == 0 :
                que.append(nx)
                visited[nx] = 1
                # 갈 수 있는 방법의 수
                board[nx] = board[x] + 1

        else :
            nx = x * dx[i]

            if 0 <= nx < 100001 and visited[nx] == 0 :
                que.append(nx)
                visited[nx] = 1
                board[nx] = board[x] + 1

print(board[m])












