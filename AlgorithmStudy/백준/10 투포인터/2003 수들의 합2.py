import sys

input = sys.stdin.readline

n,m = map(int, input().split())

a = list(map(int, input().split()))


answer = 0

for p1 in range(0,n) :
    check = 0
    for p2 in range(p1, n) :
        check += a[p2]
        if check == m :
            answer += 1
            break
        elif check > m :
            break

print(answer)




