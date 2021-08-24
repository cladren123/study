"""

괄호를 쳐서 식의 값을 최소로 만든다.

브루트 포스

eval 함수

풀이
+,- 만이 나오므로
- 기준으로 괄호를 치면 된다.

런타임에러


nlist = input().split("-")

answer = int(nlist[0])

for i in range(1,len(nlist)) :
    one = eval(nlist[i])

    answer -= one

print(answer)

"""


a = input().split('-')

num = []

for i in a :
    count = 0
    s = i.split('+')
    for j in s :
        count += int(j)

    num.append(count)


n = num[0]

for i in range(1, len(num)) :
    n -= num[i]

print(n)




