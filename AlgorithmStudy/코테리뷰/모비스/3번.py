# 3.
#
# 매달 k 일은 아파트 관리비를 내는 날입니다. 만약 그달의 k 일이 주말(토요일, 일요일)이라면 관리비는 k 일로부터 가장 가까운 평일에 냅니다.
# 한 해의 시작일인 1월 1일에 해당하는 요일 day와 매달 관리비를 내야 하는 날짜 k가 매개변수로 주어질 때,
# 그 해의 1월부터 12월까지 매달 k 일이 평일이면 0을, 주말이면 1을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1월 1일에 해당하는 요일은 다음과 같이 숫자로 주어집니다.
# 월요일: 0, 화요일: 1, 수요일: 2, 목요일: 3, 금요일: 4, 토요일: 5, 일요일: 6
# k는 1 이상 28 이하의 자연수입니다.
# 각 달의 날짜 수는 1월부터 순서대로 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 이며, 윤년과 공휴일은 고려하지 않습니다.

#######################################################################################################
day, k = map(int, input().split());                                     # day, k 입력

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];         # 각 달의 날짜 수
daysInMonth7 = list(map(lambda x: x % 7, daysInMonth));                 # 각 달의 날짜 수를 7로 나눈 나머지
print(daysInMonth7)

firstday = [day];                                                       # 각 달의 첫 째날이 무슨 요일인지 계산
for i in range(11):
    firstday.append((firstday[i] + daysInMonth7[i]) % 7);
print(firstday);

kMonth = [];                                                            # 각 달의 k일이 무슨 요일인지 계산
# for i in range(12):
#     kMonth.append((firstday[i] + (k - 1) % 7) % 7);
kMonth = list(map(lambda x: (x + (k - 1) % 7) % 7, firstday));
print(kMonth);
# print("kMonth1", kMonth1);

def func(x):                                                            # k일이 주말이면 가장 가까운 평일로 변환
    if x == 5:
        return 4;
    elif x == 6:
        return 0;
    else:
        return x;
kMonth = list(map(func, kMonth));

print(kMonth);                                                          # 정답 리스트 출력