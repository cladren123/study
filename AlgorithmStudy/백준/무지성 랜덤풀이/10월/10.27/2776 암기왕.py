

import sys


input = sys.stdin.readline


testcase = int(input())

for _ in range(testcase) :
    onedict = dict()


    n = int(input())
    one = list(map(int, input().split()))

    for i in one :
        onedict[i] = i

    m = int(input())
    two = list(map(int, input().split()))

    for i in two :
        if i in onedict :
            print(1)
        else :
            print(0)




