# 각 학생이 받은 점수의 평균을 구해 기준에 따라 학점부여
# 자기자신을 평가한 점수가 유일한 최고점이거나 유일한 최저점이면 그 점수는 제외하고 평균 구한다.
# 90점 a
# 80~90 B
# 70~80 C
# 50~70 D
# 50 F
# score의 행의 길이 : 2<= <=10
# score열의길이 = 행의길이
# score의 원소 0<= <= 100
# 입력
# [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# 결과
# "FBABD"

# min, max 값 2차원 배열
# [값, idx]
# if score[i][i] == min and min[1] > 1
# 내가 준 점수가 최소(최대) 값이고 그 점수가 유일하면
# 리스트에서 제거
# for문돌아서 평균구해
# 학점부여해

def avr(temp):
    sum = 0
    for i in range(len(temp)):
        sum += temp[i]
    avr = sum / len(temp)
    if avr >= 90:
        return 'A'
    elif 80 <= avr < 90:
        return 'B'
    elif 70 <= avr < 80:
        return 'C'
    elif 50 <= avr < 70:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    sc = [[0]*len(scores) for _ in range(len(scores))]
    for i in range(len(scores)):
         for j in range(len(scores)):
                sc[i][j] = scores[j][i]

    for i in range(len(scores)):
        temp = sc
        min = [101,0]
        max = [0,0]
        for j in range(len(scores)):
            if sc[i][j] < min[0]:
                min[0] = sc[i][j]
                min[1] = 1
            elif sc[i][j] == min[0]:
                min[0] = sc[i][j]
                min[1] += 1
            if sc[i][j] > max[0]:
                max[0] = sc[i][j]
                max[1] = 1
            elif sc[i][j] == max[0]:
                max[0] = sc[i][j]
                max[1] += 1
        if sc[i][i] == min[0] and min[1] == 1:
            del temp[i][i]
        elif sc[i][i] == max[0] and max[1] == 1:
            del temp[i][i]
        answer += avr(temp[i])
    return answer

score = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(score))
