"""
14697번 방 배정하기
중요 문제!

"""

r1, r2, r3, s = map(int, input().split())
flag = 0

for i in range(0, s+1, r1) :
    for j in range(0, s+1, r2) :
        for k in range(0, s+1, r3) :
            if i+j+k == s :
                flag = 1

print(flag)