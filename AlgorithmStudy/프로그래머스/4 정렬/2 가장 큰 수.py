from itertools import permutations

cont = ""
maxnum = 0


def solution(numbers):
    #     시간 초과가 떠버렸다.. 다른 방법으로 해보자.
    #     n = len(numbers)
    #     list1 = list(permutations(numbers, n))
    #     maxnum = 0
    #     cont = ""
    #     for i in list1 :
    #         for j in range(n) :
    #             cont += str(i[j])
    #         if maxnum <= int(cont) :
    #             maxnum = int(cont)
    #         cont = ""
    #     answer = answer + str(maxnum)

    # 시간 초과, 런타임 에러.. 어떻게 풀어야 하나
    #     n = len(numbers)
    #     used = [0] * n
    #     visited = [0] * n

    #     def solve(stage) :
    #         global maxnum
    #         global cont
    #         if stage == n :
    #             for i in used :
    #                 cont += str(numbers[i])
    #             if maxnum < int(cont) :
    #                 maxnum = int(cont)
    #             cont = ""
    #             return

    #         for i in range(n) :
    #             if visited[i] == 0 :
    #                 visited[i] = 1
    #                 used[stage] = i
    #                 solve(stage+1)
    #                 visited[i] = 0
    #     solve(0)

    #     answer = answer + str(maxnum)

    numbers = list(map(str, numbers))

    # x1 = numbers[0] * 3
    # x2 = numbers[1] * 3
    # x3 = numbers[2] * 3
    # list1 = []
    # list1.append(x1)
    # list1.append(x2)
    # list1.append(x3)
    # list1.sort(reverse=True)
    # print(list1)

    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer