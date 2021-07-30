import copy
import sys

input = sys.stdin.readline

test = int(input())

for nanana in range(test) :
    n = int(input())
    lastyear1 = list(map(int ,input().split()))
    lastyear1.insert(0,0)
    m = int(input())

    lastyear = copy.deepcopy(lastyear1)

    nlist = [[] for _ in range(n+1)]

    for _ in range(m) :
        s,e = map(int, input().split())
        nlist[e].append(s)

    print(nlist)

    clist = []

    for i in range(1, len(nlist)) :
        if nlist[i] != [] :
            for j in nlist[i] :
                clist.append(lastyear.index(j))
            clist.sort()

            one = lastyear.index(i)

            for k in clist :
                cc = lastyear[one]
                lastyear[one] = lastyear[k]
                lastyear[k] = cc
                one = k

    flag = 0
    one1 = 0
    one2 = 0


    print(lastyear1)
    print(lastyear)


    for i in range(1, len(nlist)) :
        if nlist[i] != []:
            check1 = lastyear1.index(i)
            checkx = lastyear.index(i)
            for j in nlist[i] :
                check2 = lastyear1.index(j)
                checky = lastyear.index(j)

                # print(check1, check2, checkx, checky)

                if check2 > check1 :
                    one1 = 1
                if checky > checkx :
                    one2 = 1
                if one1 == one2 :
                    flag = 1
                    break
                one1 = 0
                one2 = 0



    if flag == 1 :
        print("IMPOSSIBLE")
    elif flag == 0 :
        for i in range(1, len(lastyear)) :
            print(lastyear[i], end = " ")

    print()

