"""
1110번

"""

num1 = int(input())



one = num1 % 10
two = num1 // 10

newnumber = one + two

if newnumber >= 10 :
    newnumber = newnumber % 10

new = newnumber + one * 10

count = 1

while num1 != new :
    one = new % 10
    two = new // 10

    newnumber = one + two

    if newnumber >= 10:
        newnumber = newnumber % 10

    new = newnumber + one * 10
    count = count + 1

print(count)





