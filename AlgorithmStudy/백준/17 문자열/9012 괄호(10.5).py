"""

문제유형 :
자료구조
문자열
스택

"""

import sys

input = sys.stdin.readline

n = int(input());

for _ in range(n) :
    string = input().strip();
    string = list(string);

    check = 0;

    for word in string :
        if word == "(" :
            check += 1
        elif word == ")" :
            check -= 1

        if check == -1 :
            break

    if check == 0 :
        print("YES");
    else :
        print("NO");

