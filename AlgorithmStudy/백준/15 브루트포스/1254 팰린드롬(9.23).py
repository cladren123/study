
"""

문제유형 :
문자열
브루트포스 알고리즘

abab

ababa
a를 붙혔으니 a는 관찰할 필요가 없음

bab 랑  bab를 뒤집은거랑 비교한다

"""
import sys

input = sys.stdin.readline

words = input().strip()
n = len(words)



for i in range(n) :
    if words[i:] == words[i:][::-1] :
        print(n+i)
        break
