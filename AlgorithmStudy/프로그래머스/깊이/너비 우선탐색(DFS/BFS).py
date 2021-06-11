# 전부다 플러스로 두고 하나씩 마이너스를 바꾸면서 계산 
# 
import itertools

numbers = [1,1,1]
target = 1

def solution(numbers, target):
    maxnum = 0
    count = 0
    n = len(numbers)
    for i in numbers:
        maxnum += i

    list1 = [0,1] * n
    list2 = set(itertools.combinations(list1,n))
    print(list2)

    maxnum1 = maxnum

    for i in list2 :
        for j in range(n) :
            if i[j] == 0 :
                maxnum1 -= (numbers[j])*2
        if maxnum1 == target :
            count += 1
        maxnum1 = maxnum

    print(count)
    answer = count
    return answer

solution(numbers, target)