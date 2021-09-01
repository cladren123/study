"""
문제유형 = 스트링

포인트
시간 초과를 안뜨게 하기 위해서 매번 revserse를 하면 안된다.
reverse 가 들어올 때 flag를 이용해 여부를 확인하고 마지막에 한 번만 reverse를 사용한다.

또한 입력, 출력단에 매우 거지같은 문제이다.


"""
import sys

input = sys.stdin.readline

def do(p, arr) :
    global flag
    global n
    global rflag

    if p == 'R' :
        if rflag == 0 :
            rflag = 1
        elif rflag == 1 :
            rflag = 0

    elif p == 'D' :
        if n == 0 :
            flag = 1
        else :
            n -= 1
            if rflag == 0 :
                del arr[0]
            elif rflag == 1 :
                arr.pop()


testcase = int(input())

for _ in range(testcase) :
    flag = 0
    rflag = 0

    plist = input().strip()
    plist1 = list(plist)

    n = int(input())

    nlist = input()
    nlist1 = nlist[1:-2].split(',')

    for i in plist1 :
        do(i, nlist1)

    if rflag == 1 :
        nlist1.reverse()

    if flag == 1 :
        print('error')
    else :
        print("[", end="")
        for i in range(len(nlist1)):
            print(nlist1[i], end="")
            if i != len(nlist1) - 1:
                print(",", end="")
        print("]")





