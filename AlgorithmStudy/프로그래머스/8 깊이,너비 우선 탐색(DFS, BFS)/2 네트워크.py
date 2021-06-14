from collections import deque


def solution(n, computers):
    queue = deque()

    visited = [[0] * n for _ in range(n)]
    countline = 0

    for i in range(n):
        for j in range(i, n):
            if computers[i][j] == 1 and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                countline += 1

                while queue:
                    y, x = queue.popleft()
                    for i in range(n):
                        if computers[y][i] == 1 and visited[y][i] == 0:
                            queue.append((y, i))
                            visited[y][i] == 1
                        if computers[i][x] == 1 and visited[i][x] == 0:
                            queue.append((i, x))
                            visited[i][x] == 1

    print(countline)

    answer = countline
    return answer

networks = [[1,1,0],[1,1,0],[0,0,1]]
solution(3,networks)