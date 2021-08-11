"""
참고 사이트
https://jeongchul.tistory.com/670
구현 문제 정말 개 같다...
"""

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 모든 모양을 여기에 넣는다. 0,0 을 기준이라 생각한다.
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)],
]

def find(x,y) :
    global answer
    for i in range(19) :
        result = 0
        for j in range(4) :
            try :
                next_x = x+tetromino[i][j][0]
                next_y = y+tetromino[i][j][1]
                result += board[next_x][next_y]
            except IndexError :
                continue
        answer = max(answer, result )

def solve( ) :
    for i in range(n) :
        for j in range(m) :
            find(i,j)

answer = 0
solve()
print(answer)


