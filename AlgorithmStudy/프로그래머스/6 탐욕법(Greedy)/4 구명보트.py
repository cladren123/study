
"""
가장 작은 사람이랑 가장 큰 사람이랑 짝 지어서 하나씩 보내야 하나..?

"""


# people = [70,50,80,50]
# limit = 100

# people = [70,80,50]
# limit = 100

# people = [40,40,80]
# limit = 160

# people = [40,50,60,90]
# limit = 100

# people = [40,40,40]
# limit = 100

people = [10,20,30,40,50,60,70,80,90]
limit = 100


def solution(people, limit):
    answer = 0

    people.sort()
    print(people)
    n = len(people)

    start = 0
    last = n-1

    while True :
        if start >= last :
            break
        if people[start] + people[last] <= limit :
            people[start] = 0
            people[last] = 0
            start += 1
            last -= 1
            answer += 1
        else :
            last -= 1

    # print(people)
    for i in people :
        if i != 0 :
            answer += 1

    # print(answer)
    return answer

solution(people, limit)