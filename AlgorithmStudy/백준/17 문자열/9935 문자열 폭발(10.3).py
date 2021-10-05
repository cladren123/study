"""

문제유형 :
자료 구조
문자열
스택택
"""

import sys

input = sys.stdin.readline

# 문자열, 폭탄 입력
string = list(input().strip());
bomb = list(input().strip());

# 스택 선언
stack = [];

for i in range(len(string)) :
    # 한 글자씩 스택에 담는다.
    stack.append(string[i]);

    # 문자가 마지막 폭탄의 문자와 같으면 체크를 진행
    # 폭탄이 맞다면 폭탄의 길이만큼 스택에서 뺀다.
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb) :
        if stack[-len(bomb):] == bomb :
            for i in range(len(bomb)) :
                stack.pop()

# 남은 문자열 출력, 남은게 없다면 FRULA 출력
if stack :
    print("".join(stack));
else :
    print('FRULA')