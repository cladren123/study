
"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

테스트케이스 2번 15번 안되는 이유
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
"""


genres = ["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"]
plays = [500, 600, 500, 800, 1100, 2500, 100, 1000]
# 답 [5, 1, 4, 7, 3, 0, 6]

def solution(genres, plays):
    answer = []

    norae = dict()

    n = len(genres)

    for i in range(n) :
        if genres[i] not in norae :
            norae[genres[i]] = [[plays[i], i]]
        else :
            norae[genres[i]].append([plays[i],i])

    print(norae)


    # 지린다.. 람다를 이용한 정렬 다중 조건
    for i in norae :
        norae.get(i).sort(key=lambda x: (-x[0], x[1]))

    print(norae)
    bigo = []

    for i in norae :
        # print(i)
        # print(len(norae.get(i)))
        noraesum = 0
        for j in range(len(norae.get(i))) :
            # print(norae.get(i)[j][0])
            noraesum += norae.get(i)[j][0]
        bigo.append((noraesum,i))

    bigo.sort(reverse=True)
    print(bigo)
    for i, genre in bigo :
        if len(norae.get(genre)) >= 2 :
            for j in range(2):
                answer.append(norae.get(genre)[j][1])
        else :
            answer.append(norae.get(genre)[0][1])


    print(answer)
    return answer

solution(genres,plays)

