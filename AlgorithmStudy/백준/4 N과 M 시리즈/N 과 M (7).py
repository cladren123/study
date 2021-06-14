
n,m = map(int, input().split())

card = list(map(int, input().split()))

used = [0] * m
visited = [0] * n
card.sort()

def solve(stage) :
    if stage == m :
        for i in used :
            print(card[i], end = " ")
        print()
        return

    for i in range(n) :
        if visited[i] == 0 :
            used[stage] = i
            solve(stage + 1)
            visited[i] = 0

solve(0)