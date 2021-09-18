"""

문제유형 :
수학
브루트포스
조합론
백트랙킹킹

최소 한개의 모음과 최소 두 개의 자음을 포함해야한다.

"""
import sys
from itertools import combinations

input = sys.stdin.readline

# 입력 l : 암호로 만들 문자 수 c : 전체 문자의 수
l, c = map(int, input().split())

# 주어진 전체 문자들
alpa = list(input().strip().split())

# 정렬
alpa.sort()

# 모음을 구분하기 위해 리스트 선언
moum = ['a', 'e', 'i', 'o', 'u']

# 경우의 수를 구하기
a = list(combinations(alpa, l))

for i in a :
    answer = ""
    flag1 = 0
    flag2 = 0

    for check in i :
        # 모음이 한 개 이상인지 확인
        if check in moum :
            flag1 = 1
        # 자음이 두 개 이상인지 확인
        else :
            flag2 += 1
    
    # 조건이 충족되어야 출력
    if flag1 == 1 and flag2 >= 2 :
        for char in i :
            answer += char
        print(answer)









