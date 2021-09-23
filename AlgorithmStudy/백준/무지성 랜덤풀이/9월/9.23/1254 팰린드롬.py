

s = input()
n = len(s)

for i in range(n) :

    print(s[i:])
    print(s[i:][::-1])

    if s[i:] == s[i:][::-1] :

        print(n+i)
        break