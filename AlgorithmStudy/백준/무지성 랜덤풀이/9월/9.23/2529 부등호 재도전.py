import sys

input = sys.stdin.readline

n = int(input())
sign = input().split()

def check(left, right, sign) :
    if sign == '<' :
        return left < right
    else :
        return left > right


visited = [0] * 10

ma = ""
mi = ""

def dfs(stage, number) :
    global ma, mi

    if stage == n+1 :
        if len(mi) == 0 :
            mi = number
        else :
            ma = number
        return

    for i in range(10) :
        if visited[i] == 0 :
            if stage == 0 or check(number[-1], str(i), sign[stage-1]) :
                visited[i] = 1
                dfs(stage+1, number + str(i))
                visited[i] = 0


dfs(0, "")

print(ma)
print(mi)
















