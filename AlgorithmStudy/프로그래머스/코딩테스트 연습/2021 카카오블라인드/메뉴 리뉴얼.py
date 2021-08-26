

def solution(orders, course):
    answer = []

    n = len(orders)

    check = [0] * n

    lencheck = []

    for i in range(n) :
        m = len(orders[i])
        lencheck.append(m)


        for j in orders :
            checker = 0

            for k in range(m) :
                if orders[i][k] in j :
                    checker += 1

            if checker == m :
                check[i] += 1

    # print(lencheck)
    # print(check)

    for i in range(n) :
        if lencheck[i] in course :
            if check[i] >= 2 :
                answer.append(orders[i])

    answer.sort()
    print(answer)




    return answer



solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
solution(["XYZ", "XWY", "WXA"], [2,3,4])