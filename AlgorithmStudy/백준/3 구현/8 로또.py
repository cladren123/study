def solve(stage) :
    global num
    if stage == 6 :
        for i in used :
            print(num[i] , end = " ")
        print()
        return

    for i in range(n) :
        if stage>0 and i < used[stage-1] :
            continue
        if visited[i] == 0 :
            visited[i] = 1
            used[stage] = i
            solve(stage + 1)
            visited[i] = 0

while True :
    num = list(map(int, input().split()))
    n = num[0]
    if n == 0 :
        break
    del num[0]

    used = [0] * 6
    visited = [0] * n
    solve(0)
    print()




