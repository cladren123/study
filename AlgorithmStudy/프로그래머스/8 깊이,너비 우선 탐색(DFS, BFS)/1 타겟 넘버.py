



"""
dfs, bfs로 풀어야하는데 흠...
dfs로 풀었던거 같은데.. 재귀
"""
from itertools import product

numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target) :
    l = [(x, -x) for x in numbers]

    # print(*l)
    # print(list(product(*l)))

    # list1 =  list(map(sum, product(*l)))
    # print(list1)

    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution(numbers,target))