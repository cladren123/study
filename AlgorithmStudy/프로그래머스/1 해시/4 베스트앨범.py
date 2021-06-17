
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    _hash = {}
    for i in range(len(genres)):
        if genres[i] in _hash:
            _hash[genres[i]] += plays[i]
        else:
            _hash[genres[i]] = plays[i]

    while len(_hash) > 0:
        genre_max = max(_hash.keys(), key=(lambda k: _hash[k]))
        del (_hash[genre_max])

        second = largest = 0
        for i in range(len(genres)):
            if genres[i] == genre_max:
                if plays[i] >= largest:
                    second = largest
                    largest = plays[i]
                elif second < plays[i] < largest:
                    second = plays[i]

        answer.append(plays.index(largest))
        if second != 0:
            answer.append(plays.index(second))

    return answer

print(solution(genres,plays))