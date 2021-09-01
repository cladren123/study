


nlist = input().split("-")

answer = eval(nlist[0])


if len(nlist) >= 1 :
    for i in range(1,len(nlist)) :
        one = eval(nlist[i])

        answer -= one

print(answer)