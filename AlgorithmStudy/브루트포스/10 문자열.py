"""

1120번 문자열

자리의 개수를 파악, 앞에 붙일지 뒤에 붙일지를 결정해야한다.

발상의 전환

어떤 알파벳이든 들어올 수 있다.

작은 길이를 가진 a를 자리를 바꿔가면서 비교해서 최소값을 출력하면 된다.

"""

# 문자열은 형변환이 있어야 하나봐

a,b = input().split()

num = len(b) - len(a)
a = list(a)
b = list(b)


allsum = 0
result = []

for i in range(num+1) :
    for j in range(len(a)) :
        if a[j] != b[j+i] :
            allsum += 1
    result.append(allsum)
    allsum = 0

print(min(result))





