


import sys

input = sys.stdin.readline

string = list(input().strip());
bomb = list(input().strip());



# 스택에 담는다.
# 폭탄의 마지막 문자와 같다면 검사를 시작한다.
# 뒤에서부터 검사해서 폭탄이 맞으면 폭탄의 수만큼 pop을 실행해 폭탄을 제거한다.

stack = []

for i in range(len(string)) :
    stack.append(string[i])

    if stack[-1] == bomb[-1] and len(stack) >= len(bomb) :
        if stack[-len(bomb):] == bomb :
            for i in range(len(bomb)) :
                stack.pop()


if stack :
    print("".join(stack))
else :
    print('FRULA')








