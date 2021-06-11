def solution(array, commands):
    answer = []
    for i in commands:
        arr = array[i[0] - 1: i[1]]
        print(arr)
        arr.sort()
        print(arr)
        print(arr[i[2] - 1])
        answer.append(arr[i[2] - 1])

    return answer