# 가로가 더 길다.
# hori >= verti 가로 >= 세로
# (가로+2)*2 + 세로*2 = 브라운 타일의 수
# yellow 타일의 배열..
# 전체 타일의 수를 더해야한다.
# yellow 타일의 경우의 수를 구해서 해당되는 브라운 타일의 수를 알아야한다.
# 24인 경우 -> (1,24) (2,12) (4,6) 이렇게 경우의 수를 구해야 한다.

def solution(brown, yellow):
    garo = []
    sero = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if int(yellow / i) >= i:
                garo.append(int(yellow / i))
                sero.append(i)
    print(garo)
    print(sero)

    checksum = 0
    answer = []

    for i in range(len(garo)):
        checksum = (garo[i] + 2) * 2 + sero[i] * 2
        if checksum == brown:
            answer.append(garo[i] + 2)
            answer.append(sero[i] + 2)

    print(answer)

    return answer