"""

문제유형 :
수학
그리디 알고리즘
정렬

dfs로 풀었더니 시간초과가 발생

"""
import sys

input = sys.stdin.readline

n = int(input())

alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

def calc(al, bl) :
    answer = 0
    for i in range(n) :
        one = al[i] * bl[i]
        answer += one
    return answer

alist.sort(reverse=True)
blist.sort()

answer = calc(alist, blist)
print(answer)

"""
visited = [0] * n

def dfs(stage, case) :
    global answer
    global visited

    # 종단조건
    if stage == n :
        answer = min(answer, calc(case, blist))
        pass

    for i in range(n) :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(stage+1, case + [alist[i]])
            visited[i] = 0

dfs(0,[])
"""







