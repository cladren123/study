
"""
단순하게 생각함..
고려할 필요가 없었네..
미래는 고려할 필요가 없다.
과거만 고려하면 된디.


테스트케이스
print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)

"""

# money = [1,2,3]
# money = [1,1,4,1,4]
# money = [1000,0,0,1000,0,0,1000,0,0,1000]
# money = [1000,1,0,1,2,1000,0]
# money = [1000,0,0,0,0,1000,0,0,0,0,0,1000]
# money = [1,2,3,4,5,6,7,8,9,10]
# money = [0,0,0,0,100,0,0,100,0,0,1,1]
# money = [11,0,2,5,100,100,85,1]
money = [1,2,3]
# money = [91,90,5,7,5,7]
# money = [90,0,0,95,1,1]

def solution(money):
    n = len(money)

    dp1 = [0] * n
    dp2 = [0] * n

    print(money)

    dp1[0] = money[0]
    dp2[1] = money[1]
    dp2[2] = money[2]

    # 첫번째에서 시작

    #dp1[i-3] + money[i] dp2[i-3] + money[i]

    for i in range(2, n-1) :
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i], dp1[i-3] + money[i])

    print(dp1)
    answer = max(dp1)

    # 두번째에서 시작
    for i in range(3,n) :
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i], dp1[i-3] + money[i])

    print(dp2)

    if max(dp2) >= answer :
        answer = max(dp2)

    print(answer)

    return answer


solution(money)