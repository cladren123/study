

# m = 4
# n = 3
# puddles = [[2,2]]

# m = 2
# n = 2
# puddles = []

# m = 100
# n = 100
# puddles = []

m = 3
n = 3
puddles = [[2,2]]

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    visited = [[0] * (m + 1) for _ in range(n + 1)]


    for i in puddles :
        visited[i[1]][i[0]] = 1

    dp[1][1] = 1

    for i in dp:
        print(i)

    print()

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if dp[i][j] == 0 and visited[i][j] == 0 :
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007

    for i in dp:
        print(i)

    answer = dp[n][m]
    print(answer)

    return answer


solution(m,n,puddles)