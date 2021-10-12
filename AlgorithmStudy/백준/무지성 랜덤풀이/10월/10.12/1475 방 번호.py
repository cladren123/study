
import sys
import math

input = sys.stdin.readline

n = input().strip()

# 0~9 까지의 숫자의 개수를 담을 리스트
# 6과 9는 하나로 친다
nlist = [0] * 9

for i in n :
    if int(i) == 9 :
        nlist[6] += 1
    else :
        nlist[int(i)] += 1

nlist[6] = math.ceil(nlist[6] / 2)

print(max(nlist))



