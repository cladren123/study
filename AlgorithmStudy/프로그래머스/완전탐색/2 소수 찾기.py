import math

"""
입력값
numbers = "17"
numbers = "011"

permutations 
"""

count = 0
collect = []


def primenumber(x):
    if x == 0:
        return False
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def solution(numbers):
    global count

    def solve(stage, n, na):
        global count
        global collect
        realnum = ""
        if stage == n:
            for i in used:
                realnum += numbers[i]
                collect.append(int(realnum))
            return

        for i in range(na):
            if visited[i] == 0:
                visited[i] = 1
                used[stage] = i
                solve(stage + 1, n, na)
                visited[i] = 0

    na = len(numbers)
    # # 한자릿수의 소수 구하기
    # for i in set(numbers) :
    #     if primenumber(int(i)) :
    #         count += 1
    # print(count)
    # print()

    if na > 1:
        for i in range(2, na + 1):
            used = [0] * i
            visited = [0] * na
            solve(0, i, na)
            used.clear()
            visited.clear()

    collect2 = set(collect)

    for i in collect2:
        if primenumber(int(i)):
            count += 1

    print(count)

    answer = 0
    answer = count

    return answer