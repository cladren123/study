
"""

문제 유형 :
브루트포스알고리즘
누적합

각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램
작은 직사각형이 비슷하게 가저가야 한다.

slide share는 뭐하는 사이트인가 -> 백준님의 풀이방법이 올라와 있음
https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1451

완전탐색 - 브루트포스
case의 개수를 구함.
각 case에 해당하는 코드 작성
case들을 비교해서 가장 큰 값이 답이된다.


"""
import sys

input = sys.stdin.readline

# n : 세로 m : 가로
n, m = map(int, input().split())

# 숫자 판 입력
board = []
for _ in range(n) :
    one = input().strip()
    one = list(map(int, one))
    board.append(one)

answer = 0

# 6개의 경우를 각각 계산하자
# ▤, ▥, ㅏ,ㅜ,ㅓ,ㅗ

# ▤
for i in range(1,n-1) :
    for j in range(i+1, n) :
        s1 = sum(board[a][b] for a in range(i) for b in range(m))
        s2 = sum(board[a][b] for a in range(i,j) for b in range(m))
        s3 = sum(board[a][b] for a in range(j,n) for b in range(m))
        answer = max(answer, s1*s2*s3)

# ▥
for i in range(1,m-1) :
    for j in range(i+1, m) :
        s1 = sum(board[a][b] for a in range(n) for b in range(i))
        s2 = sum(board[a][b] for a in range(n) for b in range(i,j))
        s3 = sum(board[a][b] for a in range(n) for b in range(j,m))
        answer = max(answer,s1*s2*s3)

# ㅏ
for i in range(1,n) :
    for j in range(1,m) :
        s1 = sum(board[a][b] for a in range(n) for b in range(j)) # ㅣ왼쪽
        s2 = sum(board[a][b] for a in range(i) for b in range(j,m)) # ㅡ 위쪽
        s3 = sum(board[a][b] for a in range(i,n) for b in range(j,m)) # ㅡ 아래쪽
        answer = max(answer, s1 * s2 * s3)

# ㅜ
for i in range(1,n) :
    for j in range(1,m) :
        s1 = sum(board[a][b] for a in range(i) for b in range(m)) # ㅡ
        s2 = sum(board[a][b] for a in range(i,n) for b in range(j)) # ㅣ 왼쪽
        s3 = sum(board[a][b] for a in range(i,n) for b in range(j,m)) # ㅣ 오른쪽
        answer = max(answer, s1 * s2 * s3)

# ㅓ
for i in range(1,n) :
    for j in range(1,m) :
        s1 = sum(board[a][b] for a in range(n) for b in range(j,m)) # ㅣ 오른쪽
        s2 = sum(board[a][b] for a in range(i) for b in range(j)) # ㅡ 위쪽
        s3 = sum(board[a][b] for a in range(i,n) for b in range(j)) # ㅡ 아래쪽
        answer = max(answer, s1 * s2 * s3)

# ㅗ
for i in range(1,n) :
    for j in range(1,m) :
        s1 = sum(board[a][b] for a in range(i,n) for b in range(m)) # ㅡ 아래쪽
        s2 = sum(board[a][b] for a in range(i) for b in range(j)) # ㅣ 왼쪽
        s3 = sum(board[a][b] for a in range(i) for b in range(j,m)) # ㅣ 오른쪽
        answer = max(answer, s1 * s2 * s3)

print(answer)








