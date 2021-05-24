"""
2309번
"""

height = []

for i in range(9) :
    n = int(input())
    height.append(n)

height.sort()

used = [0] * 7
visited = [0] * 9

heightsum = 0
result = []

def solve(stage) :
    global heightsum
    global result
    global flag

    if stage == 7 :
        for i in used :
            heightsum = heightsum + height[i]
        if heightsum == 100 :
            for j in used :
                result.append(height[j])
        heightsum = 0
        return

    for i in range(9) :
        if stage > 0 and i <= used[stage-1] :
            continue
        if visited[i] == 0 :
            visited[i] = 1
            used[stage] = i
            solve(stage+1)
            visited[i] = 0

"""
stage는 자리
visited는 방문 확인용
used 에는 자릿수에 맞는 i를 집어넣게 된다. 
vvusv 
used 는 뼈대

"""


solve(0)

for i in range(7) :
    print(result[i])
