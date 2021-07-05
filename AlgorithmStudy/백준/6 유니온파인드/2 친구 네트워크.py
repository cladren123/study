



def find(friend) :
    global parent
    if friend == parent[friend] :
        return friend
    else :
        parent[friend] = find(parent[friend])
        return parent[friend]

def union(x,y) :
    global parent
    global answer
    x = find(x)
    y = find(y)
    check = parent[y]
    if x != y :
        for i in range(len(parent)) :
            if parent[i] == check :
                parent[i] = x
                answer += 1

testcase = int(input())
for test in range(testcase) :
    n = int(input())

    fnetwork = []
    parent = []
    num = 0
    answer = 1

    for i in range(n) :
        name1, name2 = input().split()

        if name1 not in fnetwork :
            fnetwork.append(name1)
            parent.append(num)
            num += 1
        if name2 not in fnetwork :
            fnetwork.append(name2)
            parent.append(num)
            num += 1

        union(fnetwork.index(name1), fnetwork.index(name2))
        print(answer)


