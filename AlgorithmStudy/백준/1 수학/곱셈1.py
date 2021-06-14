"""
2588번 곱셈
"""


num1 = int(input())
num2 = int(input())

sub1 = num2 % 10

num3 = num1 * sub1

sub2 = num2 // 10 % 10

num4 = num1 * sub2

sub3 = num2 //10 // 10 % 10

num5 = num1 * sub3

num6 = num3 + num4*10 + num5*100

print(num3)
print(num4)
print(num5)
print(num6)