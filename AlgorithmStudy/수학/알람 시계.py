hour, minu = map(int, input().split())

newhour = 0
newminu = 0

if minu >= 45 :
    newminu = minu - 45;
    newhour = hour
else :
    newminu = minu + 15
    if hour == 0 :
        newhour = 23
    else :
        newhour = hour - 1

print(newhour, newminu)



