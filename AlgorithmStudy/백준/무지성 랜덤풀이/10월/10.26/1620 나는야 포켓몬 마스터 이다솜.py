

import sys

input = sys.stdin.readline

# n : 포켓몬 개수, m : 문제의 개수
n, m = map(int, input().split())

dogam = dict()
dogam2 = dict()

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



