# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    answer = 0

    # for i in range(len(A)):
    #     if A[i] < 0:
    #         A[i] = 0

    realA = set(A)

    realA = list(realA)
    realA.sort()
    # print(realA)
    realA.append(1000001)

    # print(realA)
    count = 0

    for i in realA:
        if i > 0:
            count += 1
            # print(count)
            # print(i)

            if count != i:
                answer = count
                break

    # print(answer)

    return answer


