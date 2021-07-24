import copy
from collections import deque


def solution(tickets) :
    answer = []

    n = len(tickets)
    # print(n)

    que = deque()

    tickets.sort(key=lambda x:x[1])

    # print(tickets)

    start = 'ICN'


    for i in range(n) :
        if tickets[i][0] == start :
            checklist = []
            checklist.append(i)
            que.append([tickets[i][1],1,tickets[i], checklist])

    # print(que)

    while que :
        one = que.popleft()
        # print(one)
        start = one[0]
        number = one[1]
        answer = one[2]
        check = one[3]

        if number == n :
            break

        for i in range(n) :
            if i not in check :
                if tickets[i][0] == start :
                    newnumber = number + 1
                    answerlist = copy.deepcopy(answer)
                    answerlist.append(tickets[i][1])
                    checklist = copy.deepcopy(check)
                    checklist.append(i)
                    que.append([tickets[i][1],newnumber, answerlist, checklist])


    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

