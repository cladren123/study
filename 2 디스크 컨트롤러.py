"""
부모 n
자식 2n, 2n+1

참고사이트 : https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99

작업의 소요 시간을 기준으로 최소힙을 만들어야 한다.
[작업의 소요 시간, 작업이 요청되는 시점] 으로 앞, 뒤를 바꿔서 넣어줘야 한다.

현재 시점에서 작업을 처리할 수 있는지 여부는
작업의 요청 시간이 바로 이전에 완료한 작업의 시작 시간(start)보다 크고 현재 시점(now)보다
작거나 같아야 한다.

만약 현재 처리할 수 있는 작업이 없다면, 남아 있는 작업들의 요청 시간이 아직 오지 않은 것이기
때문에 현지 새점(now)을 하나 올려준다.

작업의 소요 시간이 가장 작은 것을 뽑는 것이 뽀인트이다!



from heapq import *

def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length

"""

import heapq

jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    # now 현재 시점
    answer, now, i = 0,0,0
    # start 이전에 완료한 작업의 시작 시간
    start = -1
    heap = []

    while i < len(jobs) :
        for j in jobs :
            if start < j[0] <= now :
                # 반대로 뒤집어서 heapq에 들어가게 된다. -> 작업의 소요 시간이 적은게 먼저 pop되게 된다.
                # 최소힙은 root node는 최소값이니까!
                heapq.heappush(heap, [j[1], j[0]])
        # heap에 들어가 있으면 실행(처리할 작업이 있는 상태)
        if len(heap) > 0 :
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            # 현재 시점 - 작업이 요청되는 시점 = 요청부터 종료까지
            answer += (now - current[1])
            i += 1
        else :
            # 처리할 작업이 없는 상태
            now += 1
    return int(answer / len(jobs))


solution(jobs)