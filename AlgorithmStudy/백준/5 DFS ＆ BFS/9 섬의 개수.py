"""
실버 2
1은 땅 0은 바다
"""
from collections import deque



while True :
    w, h = map(int, input().split())
    if w==0 and h == 0 :
        break

    # 공백이 있을 땐 split을 넣어준다.
    board = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]

    # for i in board :
    #     print(i)

    que = deque()

    way_h = [1,1,0,-1,-1,-1,0,1]
    way_w = [0,-1,-1,-1,0,1,1,1]

    count = 0

    for i in range(h) :
        for j in range(w) :
            # print(i,j)
            if board[i][j] == 1 and visited[i][j] == 0:
                que.append((i,j))
                count += 1
                visited[i][j] = count

                while que :
                    hei,wid = que.popleft()

                    for k in range(8) :
                        next_hei = hei + way_h[k]
                        next_wid = wid + way_w[k]

                        if 0 <= next_hei < h and 0 <= next_wid < w :
                            if board[next_hei][next_wid] == 1 and visited[next_hei][next_wid] == 0 :
                                que.append((next_hei, next_wid))
                                visited[next_hei][next_wid] = count

    # for i in visited :
    #     print(i)

    print(count)




