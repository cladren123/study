"""

문제유형 :
자료 구조
문자열
스택택

이중반복문을 쓰면 시간초과가 발생

"""


import sys

input = sys.stdin.readline;

# 입력단
string = input().strip();
bomb = input().strip();

while True :
    if bomb not in string :
        break;
    else :
        string = string.replace(bomb, "");

if len(string) == 0 :
    print('FRULA');
else :
    print(string);

