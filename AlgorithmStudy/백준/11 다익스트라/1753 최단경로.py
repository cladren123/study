import sys

input = sys.stdin.readline

# v 정점의 개수, e 간선의 개수
v,e = map(int, input().split())

# 시작 정점의 번호
k = int(input())

nextlist = [[] for _ in range(v+1)]

for _ in range(e) :
    s, e, w = map(int, input().split())

    nextlist[s].append([e,w])


print(nextlist)