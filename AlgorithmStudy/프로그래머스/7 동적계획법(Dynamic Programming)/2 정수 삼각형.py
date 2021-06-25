"""
어떻게 풀어야 하나...
bfs로 푸니 시간초과가 생겼다.
DP를 이용해서 풀자

[7] (0,0)
[3, 8] (1,0) (1,1)
[8, 1, 0] (2,0) (2,1) (2,2)
[2, 7, 4, 4]
[4, 5, 2, 6, 5]

"""
from collections import deque

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0

    n = len(triangle)

    for i in range(n) : # 0 1 2 3 4
        if i > 0 :
            for j in range(i+1) : # 0 01 012 0123 01234
                if j == 0 :
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j == i :
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                else :
                    triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]

    # for i in triangle :
    #     print(i)
    answer = max(triangle[n-1])
    print(answer)

    return answer

solution(triangle)