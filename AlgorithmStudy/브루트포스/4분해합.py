"""
2231번
"""


n = input()
com = int(n)

def check(n) :
    after = list(str(n))
    origin = n
    for i in after :
        origin += int(i)
    return origin

result = [0]

for i in range(com) :
    if check(i) == com :
        result.append(i)

if len(result) > 1 :
    print(result[1])
elif len(result) == 1 :
    print(result[0])












