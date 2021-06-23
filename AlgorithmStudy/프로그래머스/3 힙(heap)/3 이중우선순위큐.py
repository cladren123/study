"""
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
[0, 0]

["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
[333, -45]

heapq.nlargest(1, heap)
"""


# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

def solution(operations):
    # print(operations)
    answer = []
    stacklist = []
    answer = [0,0]

    for i in operations :
        semioper = list(i.split())
        if semioper[0] == 'I' :
            stacklist.append(int(semioper[1]))
        if len(stacklist) > 0 :
            if semioper[0] == 'D' :
                if semioper[1] == '1' :
                    stacklist.remove(max(stacklist))
                elif semioper[1] == '-1' :
                    stacklist.remove(min(stacklist))

    # print(stacklist)

    if len(stacklist) > 0 :
        maxnum = max(stacklist)
        minnum = min(stacklist)
        answer[0] = maxnum
        answer[1] = minnum

    print(answer)

    return answer


solution(operations)