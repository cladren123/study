from collections import deque

countline = 1
n = 3
computers = [[1,1,0], [1,1,0], [0,0,1]]



def solution(n, computers):
    queue = deque()

    visited = [0] * n
    countline = 1

    for i in range(n):
        computers[i][i] = 0

    def dfs(node):
        global countline

        for i in range(n):
            if computers[node][i] == 1 and visited[i] == 0:
                visited[i] = countline
                dfs(i)

    for i in range(n):
        countline += 1
        dfs(i)

    print(visited)

    countline2 = 0

    if 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                countline2 += 1
        countline2 -= 1

    num = len(set(visited))
    countline2 += num

    answer = countline2
    return answer

print(solution(n,computers))