
# 남은 날짜 계산
# 앞에게 나보다 크면 프린트

progresses1 = [93, 30, 55]
speeds1 = [1, 30, 5]
progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

"""
progresses = [85,88,87]
speeds = [1,1,1]
3
"""

progresses = [85,88,87]
speeds = [1,1,1]


def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = []

    for i in range(n) :
        day = 100 - progresses[i]
        if day % speeds[i] == 0 :
            days.append(int(day / speeds[i]))
        else :
            days.append(int(day / speeds[i]) + 1)

    count = 0
    checker = days[0]
    days.append(100)

    print(days)
    m = len(days)

    for i in range(m) :
        count += 1
        if i+1 <= m-1 and checker < days[i+1] :
            answer.append(count)
            checker = days[i+1]
            count = 0
    print(answer)

    return answer


solution(progresses,speeds)
solution(progresses1,speeds1)