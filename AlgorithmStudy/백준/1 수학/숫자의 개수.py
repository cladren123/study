A = int(input())
B = int(input())
C = int(input())



result = A * B * C

card = [0] * 10
deck = []



result1 = str(result)

for i in result1 :
    deck.append(int(i))



for i in range(0,10) :
    for j in deck :
        if i == j :
            card[i] = card[i] + 1


for i in range(10) :
    print(card[i])
