"""
10448번 유레키 이론
시간초과..?
python3은 되는데 pypy3은 정답이다.. 이게 뭐지?
"""
tri = []

m = int(input())

for i in range(m) :
    n = int(input())

    for i in range(1,n):
        if n < i*(i+1)/2 :
            continue
        tri.append(int(i*(i+1)/2))

    length = len(tri)
    used = [0] * 3
    visited = [0] * length
    allsum = 0
    flag = 0

    def solve(stage) :
        global allsum
        global flag
        if stage == 3 :
            for i in used :
                allsum += tri[i]
            if allsum == n :
                flag = 1
            allsum = 0
            return

        for i in range(length) :
            if visited[i] == 0 :
                used[stage] = i
                solve(stage + 1)
                visited[i] = 0

    solve(0)
    print(flag)
    tri.clear()


