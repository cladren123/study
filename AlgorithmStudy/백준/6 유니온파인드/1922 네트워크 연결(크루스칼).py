import sys

input = sys.stdin.readline


def find(x) :
    if x == parent[x] :
        return x
    else :
        rootx = find(parent[x])
        parent[x] = rootx
        return parent[x]

def union(x,y) :
    rootx = find(x)
    rooty = find(y)

    # 이 부분이 중요
    if rootx != rooty :
        parent[rooty] = rootx



n = int(input())
m = int(input())

wire = []

for _ in range(m) :
    wireone = list(map(int, input().split()))
    wire.append(wireone)

parent = [i for i in range(n+1)]

wire.sort(key=lambda x : x[2])

cost = 0


for i in wire :
    start = i[0]
    end = i[1]

    if find(start) != find(end) :
        union(start, end)
        cost += i[2]

print(cost)









