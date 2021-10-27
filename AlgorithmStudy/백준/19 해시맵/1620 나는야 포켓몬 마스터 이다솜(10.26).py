

import sys

input = sys.stdin.readline

# n : 포켓몬 개수, m : 문제의 개수
n, m = map(int, input().split())

# 시간복잡도를 피하기 위해 딕셔너리를 2개 사용
dogam = dict()
dogam2 = dict()

# 한개의 딕셔너리는 숫자,이름  나머지 하나는 이름,숫자 순으로 만든다.
for number in range(1,n+1) :
    name = input().strip()
    dogam[str(number)] = name
    dogam2[name] = str(number)

for _ in range(m) :
    one = input().strip()

    # 숫자인지 확인
    if one.isdigit() :
        print(dogam[one])
    else :
        print(dogam2[one])



