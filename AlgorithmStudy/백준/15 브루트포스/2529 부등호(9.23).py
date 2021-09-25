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


# 부등호 개수와 부등호를 주어진다.
input = sys.stdin.readline
n = int(input())
# input().split() 문자열을 띄어쓰기를 기준으로 리스트로 저장해준다.
giho = input().split()

# 정답을 담을 변수 선언
maxnumber = ""
minnumber = ""

# 부등호의 조건을 판별하는 함수
def check(left,right,sign) :
    if sign == '>' :
        return left > right
    else :
        return left < right

# visited 리스트로 중복되는 수가 오지 않게끔 체크한다.
visited = [0] * 10

# 재귀함수를 통해 모든 경우의 수 탐색
def dfs(stage, number) :
    global maxnumber, minnumber

    # 종단 조건건
    if stage == n+1 :
        # 처음 완성된 정수는 가장 작은 수 이다.
        if len(minnumber) == 0 :
            minnumber = number
        # 마지막으로 완성된 정수는 가장 큰 수 이다.
        else :
            maxnumber = number
        return


    # 정수를 만드는 부분
    for i in range(10) :
        if visited[i] == 0 :
            # 첫번째 단계이면 조건을 따지지 않고 실행한다.
            # 문자열의 끝부분과 다음에 들어올 수를 비교해 부등호의 조건을 만족하면 다음 수로 들어온다
            if stage == 0  or check(number[-1], str(i), giho[stage-1]) :
                visited[i] = 1
                dfs(stage+1, number + str(i))
                visited[i] = 0




dfs(0, "")
print(maxnumber)
print(minnumber)





























# 최대, 최소의 경우의 수를 만들어야 한다.


