"""
오름차순
중복 없이 M 개를 고른 수열
N개 중에 M 개를 고름
"""

n, m = map(int, input().split())

used = [0] * m
visited = [0] * n
card = []

for i in range(1,n+1) :
    card.append(i)


def solve(stage) :
    # m 개를 다 골랐으면 출력
    if stage == m :
        for i in used :
            print(card[i], end = ' ')
        print()
        return

    for i in range(n) :
        if stage > 0 and i <= used[stage-1]:
            continue;
        if visited[i] == 0 :
            visited[i] = 1;
            used[stage] = i;
            solve(stage+1)
            visited[i] = 0

            """
            0부터 n-1까지 for문이 돌아감
            visited[i] 가 0 이면 1로 바뀌면서
            used[stage]에 i가 된다.
            재귀형태로 채워지게 된다.
            visited[i] = 0 이 되면서 초기화된다.
            결국 재귀로 인해 모든 경우의 수를 탐색하게 된다. 
            """

solve(0)




