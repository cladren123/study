
"""
입력값 answers   결과값
[1,2,3,4,5] -> [1]
[1,3,2,4,2] -> [1,2,3]

"""


def solution(answers):
    student1 = [1, 2, 3, 4, 5] * 2000
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    num1 = 0
    num2 = 0
    num3 = 0

    for i in range(len(answers)):
        if answers[i] == student1[i]:
            num1 = num1 + 1
        if answers[i] == student2[i]:
            num2 = num2 + 1
        if answers[i] == student3[i]:
            num3 = num3 + 1

    print(num1, num2, num3)
    checker = max(num1, num2, num3)

    answer = []

    if checker == num1:
        answer.append(1)
    if checker == num2:
        answer.append(2)
    if checker == num3:
        answer.append(3)

    return answer