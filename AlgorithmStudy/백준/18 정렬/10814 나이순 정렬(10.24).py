

import sys

input = sys.stdin.readline

# 나이가 증가하는 순, 먼저 가입한 사람이 앞에 오는 순

n = int(input())
ndict = dict()

for _ in range(n) :
    # 이런 식으로 입력하면 age는 정수가 아니라 문자열로 들어가서 sort를 했을 때 2보다 10이 앞
    age, name = input().strip().split()
    age = int(age)
    if age in ndict :
        ndict[age].append(name)
    else :
        ndict[age] = [name]


ndict = dict(sorted(ndict.items()))


for key,value in ndict.items() :
    nv = len(value)

    for i in range(nv) :
        print(key, value[i])
