

import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m) :

    temp = input().strip().split()

    if len(temp) == 1 :
        if temp[0] == 'all' :
            s = set([i for i in range(1,21)])
        elif temp[0] == 'empty' :
            s = set()
    else :
        order, number = temp[0], temp[1]
        number = int(number)

        if order == 'add' :
            s.add(number)
        elif order == 'remove' :
            if number in s :
                s.remove(number)
        elif order == 'check' :
            if number in s :
                print(1)
            else :
                print(0)
        elif order == 'toggle' :
            if number in s :
                s.remove(number)
            else :
                s.add(number)






