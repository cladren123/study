import heapq




def solution(scoville,K):
    answer = 0

    heapq.heapify(scoville)

    # print(scoville)

    while len(scoville) >= 2 :
        minsco = heapq.heappop(scoville)

        if minsco >= K :
            return answer
        else :
            answer += 1
            minsco2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (minsco + minsco2*2))
        # print(scoville)

    if scoville[0] > K :
        return answer
    else :
        answer = -1
        return answer

    return answer

scoville = [1,2,3,9,10,12]
K = 7

print(solution(scoville,K))