"""

문제유형 :
브루트포스
백트래킹

0~9 총 10개의 숫자
우선순위를 부여해야한다.

브루트포스, n과 m, dfs

조건과 경우의 수,

"""
import sys

input = sys.stdin.readline

n = int(input())

# input().split() 문자열을 띄어쓰기를 기준으로 리스트로 저장해준다.
giho = input().split()

maxnumber = ""
minnumber = ""

def check(left,right,sign) :
    if sign == '>' :
        return left > right
    else :
        return left < right

visited = [0] * 10

def dfs(stage, number) :
    global maxnumber, minnumber

    # 종단 조건건
    if stage == n+1 :
        if len(minnumber) == 0 :
            minnumber = number
        else :
            maxnumber = number
        return


    for i in range(10) :
        if visited[i] == 0 :
            if stage == 0  or check(number[-1], str(i), giho[stage-1]) :
                visited[i] = 1
                dfs(stage+1, number + str(i))
                visited[i] = 0


dfs(0, "")
print(maxnumber)
print(minnumber)





























# 최대, 최소의 경우의 수를 만들어야 한다.


