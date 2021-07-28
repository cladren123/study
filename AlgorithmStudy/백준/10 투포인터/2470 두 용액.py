import sys

input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))

nl.sort()

# print(nl)

s = 0
e = n-1
one = sys.maxsize


finals = 0
finale = 0


while True :
    check = nl[s] + nl[e]
    if one > abs(check) :
        one = abs(check)
        finals = nl[s]
        finale = nl[e]

    if check < 0 :
        s += 1
    else :
        e -= 1

    if s == e :
        break

print(finals, finale)




















