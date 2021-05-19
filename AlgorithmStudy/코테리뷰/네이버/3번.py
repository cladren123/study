# 전문가 감정
#4가지 방법으로 판매가 결정
#1번부터 적용시킬 수 있으면 시키고 없으면 다음 방법으로
#1. 가장 비싼 가격 과 가잔 싼 가격의 차가 d원 이하라면 모든 제시 가격의 평균가로 판매가 결정
#2. 가장 비싼 가격 하나, 가장 싼 가격 하나 제외, 나머지 가격 중 가장 비싼 가격과 가장 싼 가격의 차가 d원 이하면 남은 가격의 평균으로 판매가 결정
#3. 임의로 k개의 가격을 골랐을 때 가장 비싸게 책정한 가격과 가장 싸게 책정한 가격의 차가 d원 이하라면 그 k개의 가격의 평균으로 판매가 결정, 정당한 가격을 책정한 k개의 가격을 고르는 방법이 여러 개라면, 그중에서 평균값이 가장 낮은 것을 판매가로 결정
#4. 중앙값을 판매가로 결정, 오름차순으로 정렬해서 가운데 위치하는 가격 판매가로, 가격의 개수가 짝수라면, 가운데 위치하는 두 가격 중에 크지 않은 가격을 판매가로 결정
#* 평균값 구할 때 모든 소수점 이하는 버리기
#3 <= prices의 길이 <= 1,000,000
#1<= prices의 원소<= 2,000
#0<= d <= 2,000
#1<= k <= price의 길이
#입출력1
#prices = [4,5,6,7,8]
#d = 4, k = 3, result = 6
#입출력2
#prices = [1,8,1,8,1,8]
#d = 6, k = 4, result = 1
from statistics import median_low
from itertools import combinations
from copy import copy


def minmax(temp):
    max = 0
    min = 2001
    for i in range(len(temp)):
        if temp[i] < min:
            min = temp[i]
        if temp[i] > max:
            max = temp[i]
    return min, max

def avr(temp):
    sum = 0
    for i in range(len(temp)):
        sum += temp[i]
    return sum // len(temp)

def solution(prices, d, k):
    answer = 0
    temp = copy(prices)
    min, max = minmax(temp)
    if max - min <= d: ## 1
        answer = avr(prices)
    else: ## 2
        del temp[temp.index(max)]
        del temp[temp.index(min)]
        min, max = minmax(temp)
        if max - min <= d: ## 2
            answer = avr(temp)
        else: ##3
            minans = 2001
            avglist = []
            com = list(combinations(prices,k))
            for c in com:
                min, max = minmax(c)
                if max - min <= d: ## 2
                    tempans = avr(c)
                    if tempans < minans:
                        minans = tempans
                    answer = minans
                else:
                    answer = median_low(prices)
    return answer