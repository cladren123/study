
n = int(input())

candy = []
result = []

for i in range(n) :
    a = list(input())
    candy.append(a)


def check(candy) :
    a = 1
    b = 1
    for i in range(n) :
        for j in range(n) :
            if j+1 < n :
                if candy[i][j] == candy[i][j+1] :
                    a += 1
                else :
                    result.append(a)
                    a = 1
                if candy[j][i] == candy[j+1][i] :
                    b += 1
                else :
                    result.append(b)
                    b = 1
        result.append(a)
        result.append(b)
        a=1
        b=1

check(candy)


for i in range(n) :
    for j in range(n) :
        if j+1 < n :
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            check(candy)
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            check(candy)
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]




print(max(result))


