"""

문제유형 :
브루트포스 알고리즘

아홉 개의 수 중 합이 100이 되는 일곱개의 수를 찾자.

"""
import sys

input = sys.stdin.readline

nlist = []

for _ in range(9) :
    nlist.append(int(input()))

# 숫자가 쓰였음을 체크하는 리스트
visited = [0] * 9

def dfs(stage, idx, alist) :
    # 종단 조건
    if stage == 7 :
        if sum(alist) == 100 :
            for i in alist :
                print(i)
        return

    for i in range(idx,9) :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(stage + 1, i, alist + [nlist[i]])
            visited[i] = 0

dfs(0,0,[])


















