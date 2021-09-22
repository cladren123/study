"""

문제유형 :
그리디 알고리즘
브루트포스 알고리즘

우선순위 매김
우선순위에 따라 숫자 부여
계산


"""
import operator
import sys
from collections import defaultdict
from itertools import permutations

input = sys.stdin.readline

# n 단어의 개수
n = int(input())

words = []

# 문자열을 받은 것을 리스트로 변환한 다음 리스트에 담는다.
for _ in range(n) :
    one = input().strip()
    one = list(one)
    words.append(one)

# 단어의 중요도
# 100과 1의 자리에 있다면 101로 저장
worddict = {}

for case in words :
    ncase = len(case)-1

    for word in case :
        if word in worddict :
            one = worddict.get(word)
            one += 10**ncase
            worddict[word] = one
        else :
            worddict[word] = 10**ncase

        ncase -= 1


# 자릿값이 높은 순서대로 높은 숫자를 부여한다.
# 딕셔너리를 value을 기준으로 오름차순으로 정렬한다.
worddict = dict(sorted(worddict.items(), key = operator.itemgetter(1), reverse=True))
number = 9
for i in worddict :
    worddict[i] = number
    number -= 1


# 단어를 숫자로 변환한 다음 계산한다.
alist = []

for word in words :
    transnumber = 0
    nword = len(word)-1
    for letter in word :
        one = worddict.get(letter) * (10**nword)
        transnumber += one
        nword -= 1
    alist.append(transnumber)

print(sum(alist))























