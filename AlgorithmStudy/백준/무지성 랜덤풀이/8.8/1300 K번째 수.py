"""
골드 3
문제 유형 : 이분 탐색

메모리 초과

"""
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

# graph = [[0] * (n+1) for _ in range(n+1)]
oneline = []

count = 0

for i in range(n+1) :
    for j in range(n+1) :
        # graph[i][j] = i*j
        if i >0 and j >0 :
            oneline.append(i*j)

# for i in graph :
#     print(i)

oneline.sort()

print(oneline[k])



