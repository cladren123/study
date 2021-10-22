
import sys

input = sys.stdin.readline

# n 중에서 m개를 골라
n,m = map(int, input().split())

card = []
for i in range(n) :
    card.append(i+1)

visited = [0] * n

hubo = []

def dfs(stage, hubo) :
    #
    if stage == m :
        print(*hubo)
        pass

    for i in range(n) :
        if visited[i] == 0 :
            visited[i] = 1
            hubo.append(i+1)
            dfs(stage+1, hubo)
            hubo.remove(i+1)
            visited[i] = 0

dfs(0,[])





