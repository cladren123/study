from collections import deque

priorities = [2,1,3,2]
location = 2

priorities2 = [9,1,1]
location2 = 0

def solution(priorities, location):
    answer = 0
    que = deque()

    maxnum = max(priorities)

    for i in range(len(priorities)) :
        que.append((priorities[i], i))

    print(que)
    answerlist = []
    count = 1

    while que :
        checker = 0
        maxnum2 = 0
        pri, loc = que.popleft()
        if pri == maxnum :
            answerlist.append((loc,count))
            count += 1
            for i in que :
                if maxnum == i[0] :
                    checker += 1
                if maxnum2 <= i[0] :
                    maxnum2 = i[0]
            if checker == 0 :
                maxnum = maxnum2
        else :
            que.append((pri, loc))
    for i in answerlist :
        if i[0] == location :
            answer = i[1]
    print(answer)
    return answer


solution(priorities,location)
solution(priorities2,location2)

"""
from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque()
    for i in range(len(priorities)):
        que.append([priorities[i],i])
    #print(que)
    while len(que):
        j, idx = que.popleft()
        maxp = 0
        for k in range(len(que)):
            if que[k][0] > maxp:
                maxp = que[k][0]
        if len(que) != 0 and maxp > j:
            que.append([j,idx])
        else:
            answer += 1
            if idx == location:


"""