

import sys

input = sys.stdin.readline


# n : 듣도 못한 사람 수, m : 보도 못한 사람 수
n, m = map(int, input().split());

ndict = dict();

for _ in range(n) :
    one = input().strip();
    ndict[one] = 1;

for _ in range(m) :
    one = input().strip();

    if one in ndict :
        ndict[one] = ndict.get(one) + 1;
    else :
        ndict[one] = 1;

alist = []

for key, value in ndict.items() :
    if value == 2 :
        alist.append(key)

# 숫자와 이름을 사전순으로 출력
alist.sort()
print(len(alist))
for i in alist :
    print(i)


