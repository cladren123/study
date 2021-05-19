# 2.
#
# 당신은 송아지 한 마리를 키우고 있습니다. 지금부터 n일 이내에 이 송아지를 반드시 먼저 팔고 새로운 송아지를 한 마리 사야만 합니다.
# 송아지 가격은 하루 단위로 갱신되며, 같은 가격으로 유지될 수도 있습니다. 다행히 n일 간의 송아지 가격은 정확히 예측됩니다.
# 당신은 판매 이익(판매가격 - 구매가격)이 최대가 되도록 판매일과 구매일을 잡아야 합니다. 단, 같은 날에 송아지를 팔고 살 수는 없습니다.
# 예1) n = 10 이고, 이 기간 동안 송아지 가격이 3, 1, 4, 1, 5, 9, 2, 6, 5, 3 원으로 예측되면,
# 6 일째 되는 날 송아지를 팔고 7 일째 되는 날 송아지를 사는 것이 가장 유리합니다 (9 - 2 = 7 원 이익).
#
# 예2) n = 10 이고, 이 기간 동안 송아지 가격이 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 원으로 예측되면,
# 10 일 이전에 아무 날이나 팔고 바로 그 다음 날 사는 것이 가장 유리합니다 (-1 원 이익, 즉 1 원 손실).
#
# 당신이 송아지를 팔고 사야하는 기간 n, 그리고 이 기간 중의 송아지 값을 담은 배열 v 가 매개변수로 주어질 때,
# 최대 판매 이익을 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# n은 2 이상 1,000,000 이하인 자연수입니다.
# v는 길이가 n인 정수형 배열입니다.
# v의 원소는 송아지 값을 나타나며, 1 이상 1,000,000,000 이하인 자연수입니다.

#####################################################################################################################
def solution(n, v):                      # 솔루션 함수
    max = None; f = 0; r = 0;

    for i in range(n):                   # front, rear를 두고 반복문 시작
        r += 1;                          # f, r 0으로 초기화 했으므로 r에 1을 더하여 검사 시작
        if r < n:                        # r이 n보다 작은 경우에만 실행
            temp = v[f] - v[r];          # f에서 r을 뺀다
            if v[f] < v[r]:              # 다음날 가격이 증가한 경우 f을 r의 위치로 당긴다. 이 때 max가 None이면 max 초기화 시켜준다.
                f = r;
                if max == None:
                    max = temp;
            else:                        # 다음날 가격이 감소한 경우 f에서 r을 뺀 값이(temp) max보다 크면 바꾼다.
                if max == None:
                    max = temp;
                else:
                    if max < temp:
                        max = temp;
    return max;


v1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3];
v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

n = int(input("n입력: "));                # 입력
v = v2;

max = solution(n, v);                    # 함수 호출
print(max);