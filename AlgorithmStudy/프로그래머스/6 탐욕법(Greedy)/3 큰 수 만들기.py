"""
n과 m 문제

combinations 를 입으면 시간초과가 뜬다.

마지막 12번 케이스
number = "1000"
k = 1
"""
from itertools import combinations

# number = "1924"
# k = 2

# number = "1231234"
# k = 3

# number = "4177252841"
# k = 4

number = "1000"
k = 1

def solution(number, k):
    answer = ""
    newk = k+1

    n = len(number)
    check = [0]

    for i in range(n) :
        num = int(number[i])
        j = -1
        if newk == 0 :
            check.append(num)
        else :
            if num > check[j] and newk != 0 :
                while True :
                    del check[j]
                    newk -= 1
                    if len(check) == 0 or newk == 0 :
                        check.append(num)
                        break
                    if check[j] >= num :
                        check.append(num)
                        break
            elif check[j] >= num :
                check.append(num)
    while newk :
        del check[-1]
        newk -= 1

    for i in check :
        answer += str(i)

    print(answer)

    return answer

solution(number,k)