


def find(x) :
    if x == parents[x] :
        return x
    else :
        rootx = find(parents[x])
        parents[x] = rootx
        return parents[x]

def union(x,y) :
    rootx = find(x)
    rooty = find(y)

    if rootx != rooty :
        parents[rooty] = rootx
        number[rootx] += number[rooty]

test_cases = int(input())

for _ in range(test_cases) :
    parents = dict()
    number = dict()
    n = int(input())


    for _ in range(n) :
        f1, f2 = input().split()
        parents[f1] = f1
        parents[f2] = f2
        union(f1, f2)

        count = 0
        for i in parents :
            if parents[i] == f2 :
                count += 1

        print(parents)
        print(count)












