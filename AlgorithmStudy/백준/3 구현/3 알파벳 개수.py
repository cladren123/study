

s = input()

card = [0] * 26

for i in s :
    card[ord(i)-97] += 1

for i in card :
    print(i, end = " ")
