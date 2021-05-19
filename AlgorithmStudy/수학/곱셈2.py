"""
곱셈2
10 * 11 / 12
재귀함수
10^5 를 미리 구한다.
B가 짝수인 경우
10^10 -> (10^5)^2 -> (10^5) * (10^5)
B가 홀수인 경우
10^11 -> (10^5)^2 * 10 -> (10^5) * (10^5) * 10
B가 1이 되면 A%C를 리턴하자
"""
A, B, C = map(int, input().split())

def multi(A,B,C) :
    if B == 1 :
        return A % C
    else :
        temp = multi(A,B//2,C)
        if B % 2 == 0 :
            return temp * temp % C
        elif B % 2 == 1 :
            return temp * temp * A % C

print(multi(A,B,C))
