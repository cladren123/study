import sys

input = sys.stdin.readline

n, m = map(int, input().split())

wire = []

for _ in range(m) :
    wireone = list(map(int, input().split()))
    wire.append(wireone)


parent = [i for i in range(n+1)]
# print(parent)

def find(x,parent) :
    if parent[x] == x :
        return x
    else :
        parent[x] = find(parent[x], parent)
        return parent[x]


def union(x,y,parent) :
    x = find(x,parent)
    y = find(y,parent)

    if x != y :
        parent[x] = y
        return 1
    else :
        return 0




wire.sort(key=lambda x:x[2])

# print(wire)

allcost = 0

costlist = []
lastcost = 0

for wireone in wire :
    start = wireone[0]
    end = wireone[1]
    cost = wireone[2]

    check = union(start,end,parent)
    if check == 1 :
        allcost += cost
        lastcost = cost


print(allcost - lastcost)






