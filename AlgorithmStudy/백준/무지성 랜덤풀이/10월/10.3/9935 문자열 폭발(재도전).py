

import sys

input = sys.stdin.readline

string = list(input().strip());
bomb = list(input().strip());

stack = [];

for i in range(len(string)) :
    stack.append(string[i]);

    if stack[-1] == bomb[-1] and len(stack) >= len(bomb) :
        if stack[-len(bomb):] == bomb :
            for i in range(len(bomb)) :
                stack.pop()


if stack :
    print("".join(stack));
else :
    print('FRULA')



