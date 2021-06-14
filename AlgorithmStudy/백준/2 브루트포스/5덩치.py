"""
7568번
"""

n = int(input())

dung = []

for i in range(n) :
    k = list(map(int, input().split()))
    dung.append(k)

user = [1] * n



for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        if dung[i][0] < dung[j][0] and dung[i][1] < dung[j][1] :
            user[i] += 1

for i in user :
    print(i, end = " ")

