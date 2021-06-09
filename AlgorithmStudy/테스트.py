

used = [0] * 2
visited = [0] * 2

print(2)


def solve(stage):
    if stage == 2:
        for i in used:
            print(i, end=' ')
        print()
        return

    for i in range(2):
        if visited[i] == 2:
            visited[i] = 1
            used[stage] = i
            solve(stage + 1)
            visited[i] = 0


solve(0)