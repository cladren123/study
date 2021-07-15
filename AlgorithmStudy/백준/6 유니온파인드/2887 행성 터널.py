
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

    if rootx != rooty :
        parent[rooty] = rootx




n = int(input())
plant = [0]

check = [i for i in range(2,n+1)]
print(check)

for _ in range(n) :
    plantone = list(map(int, input().split()))
    plant.append(plantone)

visited = [0] * (n+1)
allcost = 0

checker = []
bestmincost = 0

for i in check :
    mincost = min(abs(plant[1][0] - plant[i][0]),abs(plant[1][1] - plant[i][1]),abs(plant[1][2] - plant[i][2]))
    checker.append([i,mincost])
    if bestmincost > mincost :
        bestmincost = mincost



for j in checker










