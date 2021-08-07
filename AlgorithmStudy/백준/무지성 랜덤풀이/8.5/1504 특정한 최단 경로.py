
# 문제 유형 : 다익스트라 알고리즘

"""
1번에서 n번 정점 최단거리 이동
두 정점을 반드시 통과..

"""

import sys

input = sys.stdin.readline

n,e = map(int, input().split())

road = []

for _ in range(e) :
    one = list(map(int, input().split()))
    road.append(one)

v1, v2 = map(int, input().split())

heap = []












