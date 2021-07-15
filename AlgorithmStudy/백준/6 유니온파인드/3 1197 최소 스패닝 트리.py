
def find(x) :
    if x == parent[x] :
        return x
    else :
        rootx = find(parent[x])
        parent[x] = rootx
        return parent[x]

def union(x,y) :
    if find(x) != find(y) :
        parent[find(y)] = find(x)



v, e = map(int, input().split())

cost = 0
parent = [i for i in range(v+1)]
wire = []

for _ in range(e) :
    wireone = list(map(int, input().split()))
    wire.append(wireone)

wire.sort(key=lambda x : x[2])


for i in wire :
    start = i[0]
    end = i[1]

    if find(start) != find(end) :
        union(start,end)
        cost += i[2]

print(cost)





