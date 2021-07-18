from collections import deque

# n = 3
# computer = [[1,1,0], [1,1,0], [0,0,1]]

n = 3
computer = [[1,1,0], [1,1,1], [0,1,1]]


def solution(n, computer) :

    print(n, computer)

    parent = [0] * n

    que = deque()
    visited = [[0] * n for _ in range(n)]
    visitedcomputer = [0] * n

    count = 0


    for i in range(0,n) :
        for j in range(0,n) :
            if i == j :
                continue
            if computer[i][j] == 1 and visited[i][j] == 0 :
                visited[i][j] = 1
                que.append([i,j])
                visitedcomputer[i] = 1
                visitedcomputer[j] = 1

                count += 1

                while que :
                    node1, node2 = que.popleft()

                    for k in range(n) :
                        if computer[node2][k] == 1 and visited[node2][k] == 0 :
                            visitedcomputer[k] = 1
                            visited[node2][k] = 1
                            que.append([node2,k])


    netnet = visitedcomputer.count(0)
    answer = netnet + count

    # print(count)
    # print(netnet)
    # print(answer)

    return answer

solution(n,computer)