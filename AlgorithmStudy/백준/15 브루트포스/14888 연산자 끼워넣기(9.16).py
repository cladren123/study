"""

문제유형 :
브루트포스 알고리즘
백트랙킹

식의 결과가 최대인 것과 최소인 것을 구하자.

"""
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

# 순서대로 + - * / 의 개수
gihonum = list(map(int, input().split()))

maxanswer = -sys.maxsize
minanswer = sys.maxsize

giho = []

for i in range(4) :
    for j in range(gihonum[i]) :
        if i == 0 :
            giho.append("+")
        elif i == 1 :
            giho.append("-")
        elif i == 2 :
            giho.append("*")
        elif i == 3 :
            giho.append("/")

giholist = list(permutations(giho,len(giho)))

for gi in giholist :
    answer = 0
    bri = number[0]
    for i in range(n-1) :
        if gi[i] == '+' :
            bri = bri + number[i+1]
        elif gi[i] == '-' :
            bri = bri - number[i+1]
        elif gi[i] == '*' :
            bri = bri * number[i+1]
        elif gi[i] == '/' :
            if bri < 0 :
                bri = bri * (-1)
                bri = bri // number[i+1]
                bri = bri * (-1)
            else :
                bri = bri // number[i+1]

    answer = bri

    maxanswer = max(maxanswer, answer)
    minanswer = min(minanswer, answer)


print(maxanswer)
print(minanswer)