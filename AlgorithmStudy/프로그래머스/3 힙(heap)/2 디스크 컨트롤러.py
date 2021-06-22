"""
부모 n
자식 2n, 2n+1

"""

import heapq

jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    answer = 0
    time = 0
    checktime = 0


    # for i in jobs :
    #     i[0], i[1] = i[1], i[0]

    heapq.heapify(jobs)

    timelist = []

    while len(jobs) :
        time += jobs[checktime][1]
        timelist.append(time - jobs[checktime][0])

        if time >= jobs[checktime+1][0] and time >= jobs[checktime+2][0] :
            if jobs[checktime+1][1] <= jobs[checktime+2][1] :
                time += jobs[checktime+1][1]
                timelist.append(time - jobs[checktime+1][0])
                time += jobs[checktime + 2][1]
                timelist.append(time - jobs[checktime + 2][0])
            else :
                time += jobs[checktime + 2][1]
                timelist.append(time - jobs[checktime + 2][0])
                time += jobs[checktime + 1][1]
                timelist.append(time - jobs[checktime + 1][0])
        else :
            time += jobs[checktime + 1][1]
            timelist.append(time - jobs[checktime + 1][0])
            time += jobs[checktime + 2][1]
            timelist.append(time - jobs[checktime + 2][0])

        heapq.heappop(jobs)
        heapq.heappop(jobs)
        heapq.heappop(jobs)

    print(timelist)
    answer = int(sum(timelist)/len(timelist))
    print(answer)





    return answer


solution(jobs)