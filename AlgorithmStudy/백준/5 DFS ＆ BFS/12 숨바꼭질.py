
"""
61퍼에서 오답처리됨..
# n 수빈의 위치 k 동생의 위치
n,k = map(int, input().split())

board = [-1] * 100001
visited = [-1] * 100001

way = [-1,1,2]
que = deque()
que.append(n)
board[n] = 0
visited[n] = 1

while que :
    cur = que.popleft()

    for i in range(3) :
        if i < 2 :
            next = cur + way[i]
            if 0 < next < 100001 and visited[next] == -1  :
                que.append(next)
                visited[next] = 1
                board[next] = board[cur] + 1


        else :
            next = cur * way[i]
            if 0 < next < 100001 and visited[next] == -1 :
                que.append(next)
                visited[next] = 1
                board[next] = board[cur] + 1


print(board[k])
# print(board)
# print(visited)

구글링을 해버렸다.
출저 : https://wook-2124.tistory.com/273

"""

from collections import deque

# 이동하는 거릴ㄹ 알기 위한 변수
max = 10 ** 5
dist = [0] * (max+1)

n,k = map(int, input().split())

que = deque()
que.append(n)

# 종단 조건을 주는게 중요한 포인트 같다.

while que :
    x = que.popleft()
    if x == k :
        print(dist[x])
        break
    for nx in (x-1, x+1, x*2) :
        if 0 <= nx <= max and not dist[nx] :
            dist[nx] = dist[x] + 1
            que.append(nx)





