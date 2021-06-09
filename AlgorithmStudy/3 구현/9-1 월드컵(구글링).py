

from itertools import combinations
import sys

input = sys.stdin.readline

def solve(round) :
    global ans
    if round == 15 :
        ans = 1
        for sub in res :
            if sub.count(0) != 3 :
                ans = 0
                break
        return

    t1, t2 = game[round]
    for x,y in ((0,2), (1,1), (2,0)) :
        if res[t1][x] > 0 and res[t2][y] > 0 :
            res[t1][x] -= 1
            res[t2][y] -= 1
            solve(round + 1)
            res[t1][x] += 1
            res[t2][y] += 1

answer = []
game = list(combinations(range(6),2))

for tc in range(4) :
    tmp = list(map(int, input().split()))

    # tmp에서 받은 것을 3개씩 묶어주는 기능
    res = [tmp[i:i+3] for i in range(0,16,3)]
    ans = 0
    solve(0)
    answer.append(ans)

print(*answer)
