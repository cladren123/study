"""
14889번 : 스타트와 링크
"""

n = int(input())
s = []

for i in range(n) :
    i = list(map(int, input().split()))
    s.append(i)


newn = int(n/2)

used = [0] * newn
visited = [0] * n

start = 0
link = 0
check1 = []
check2 = 0

allsum = 0
for i in range(n) :
    for j in range(n) :
        allsum += s[i][j]





def solve(stage) :
    global start
    global link
    global check1
    global check2
    usedsum1 = 0
    usedsum2 = 0
    used2 = []
    for i in range(n):
        used2.append(i)
    if stage == n/2 :
        for i in used :
            used2.remove(i)

        for i in used :
            for j in used :
                usedsum1 += s[i][j]

        for i in used2 :
            for j in used2 :
                usedsum2 += s[i][j]

        check1.append(abs(usedsum1-usedsum2))
        return

    for i in range(n) :
        if stage > 0 and i < used[stage-1] :
            continue
        if visited[i] == 0 :
            visited[i] = 1
            used[stage] = i
            solve(stage + 1)
            visited[i] = 0

solve(0)

check1.sort()
print(check1[0])



