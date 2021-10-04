"""

문제유형 :
수학
정수론
유클리드 호재법

유클리드 호재법
최대공약수 MOD 연산 반복



"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

bignumber = max(n,m);
smallnumber = min(n,m);

# 유클리드 호재법 - 최대공약수 구하기


while True :
    check = bignumber % smallnumber

    if check == 0 :
        gongyak = smallnumber
        break

    bignumber = smallnumber
    smallnumber = check

gongbae = gongyak * (n//gongyak) * (m//gongyak)

print(gongyak)
print(gongbae)






