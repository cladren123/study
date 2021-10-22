
import sys

input = sys.stdin.readline


n = int(input())

adict = dict()

for _ in range(n) :
    one = input().strip()

    if one in adict :
        adict[one] = adict.get(one) + 1
    else :
        adict[one] = 1

adict = dict(sorted(adict.items(), key = lambda x : (-x[1], x[0])))

# 첫번째 값을 출력하려면 리스트로 만든다음 선택
print(list(adict.keys())[0])


