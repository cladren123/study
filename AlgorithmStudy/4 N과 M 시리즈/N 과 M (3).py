
"""
N 개 중에 M 개를 선택
같은 수를 여러번 골라도 된다.
15651 번
"""

n, m = map(int, input().split())

used = [0] * m
visited = [0] * n
card = []
for i in range(1,n+1) :
    card.append(i)

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
