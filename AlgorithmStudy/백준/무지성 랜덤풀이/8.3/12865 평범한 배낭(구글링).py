"""
출저 : https://claude-u.tistory.com/208

"""
import sys

input = sys.stdin.readline


# n : 물품의 수, k : 버틸 수 있는 무게
n, k = map(int, input().split())

stuff = [[0,0]]

# 가로 : 무게, 세로 : 물품의 수 2차원 배열을 생성한다.
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

# 물건의 무게, 가치를 저장하는 리스트
for _ in range(n) :
    stuff.append(list(map(int, input().split())))


# 냅색 문제 풀이

# i는 세로, 물건의 갯수 만큼 돈다.
for i in range(1, n+1) :
    # j는 가로, 무게의 수 만큼 돈다. 무게가 수용할 수 있는 최대 가치를 저장한다.
    for j in range(i, k+1) :
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight :
            # weight 보다 작으면 위의 값을 그대로 가져온다.
            knapsack[i][j] = knapsack[i-1][j]

            # weight 보다 크면, 즉 수용할 수 있는 무게가 들어오면
            # 현재 탐색중인 물건의 가치 + 현재 탐색중인 무게의 - 현재 탐색중인 물건의 무게를 뺀 값 즉 남은 무게에
            # 값이 있다면 두 개의 값을 더한 것과, 이전의 해당 무게의 값과 비교를 해서 큰 값을 저장한다.
        else :
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

# print(stuff)
# for i in knapsack :
#     print(i)

# 마지막에 오는게 가장 큰 가치가 된다.
print(knapsack[n][k])