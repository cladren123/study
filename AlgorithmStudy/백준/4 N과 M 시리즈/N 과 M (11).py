

n,m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

used = [0] * m
visited = [0] * n

def solve(stage) :
    check = 0
    if stage == m :
        for i in used :
            print(card[i], end = " ")
        print()
        return

    for i in range(n) :
        if check != card[i] :
            check = card[i]
            used[stage] = i
            solve(stage + 1)
            visited[i] = 0

solve(0)