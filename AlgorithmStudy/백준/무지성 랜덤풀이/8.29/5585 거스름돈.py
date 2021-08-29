"""

문제 유형 : 그리디

"""
import sys

input = sys.stdin.readline

n = int(input())

gibon = 1000

jandon = [500,100,50,10,5,1]

target = gibon - n

answer = 0

for i in jandon :
    answer += target // i
    target = target % i
    if target == 0 :
        break

print(answer)
