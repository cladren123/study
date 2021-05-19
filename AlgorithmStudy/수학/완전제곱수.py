"""
1977번

문제풀이 :
완전제곱수를 배열에 놓고 비교하면서 구하자

"""


M = int(input())
N = int(input())

num = []
result = []

i = 1
while i <= N**(1/2) :
    num.append(i*i)
    i = i + 1



for i in num :
    if M <= i <= N :
        result.append(i)



if len(result) == 0:
    print(-1)
else :
    print(sum(result))
    print(result[0])



