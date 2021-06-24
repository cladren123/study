
# n = 5
# lost = [2,4]
# reserve = [1,3,5]

# n = 5
# lost = [2,4]
# reserve = [3]

n = 3
lost = [3]
reserve = [1]


def solution(n, lost, reserve):
    answer = 0

    visited = [1] * (n+1)
    for i in lost :
        visited[i] = 0
    for i in reserve :
        visited[i] += 1

    print(visited)

    for i in range(len(visited)) :
        if visited[i] == 0 :
            if visited[i-1] == 2 :
                visited[i-1] -= 1
                visited[i] += 1
            elif i+1 < len(visited) :
                if visited[i+1] == 2 :
                    visited[i+1] -= 1
                    visited[i] += 1

    print(visited)

    lostperson = visited.count(0)
    answer = n - lostperson

    print(answer)

    return answer

solution(n,lost,reserve)