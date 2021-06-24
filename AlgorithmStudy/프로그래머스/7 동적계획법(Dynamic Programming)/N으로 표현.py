"""
+,-,*,/
자릿수

https://gurumee92.tistory.com/164
"""


N = 5
number = 12


def solution(N, number):
    answer = 0

    if N == number :
        return 1

    s = [ set() for x in range(8) ]
    print(s)

    for i,x in enumerate(s, start=1) :
        print(i,x)
        x.add( int(str(N)*i))

    print(N, number)

    dp = []



    return answer

solution(N,number)