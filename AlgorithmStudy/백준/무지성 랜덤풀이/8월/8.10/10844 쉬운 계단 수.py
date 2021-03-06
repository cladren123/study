import sys

input = sys.stdin.readline


n = int(input())

"""
DP

1 2 3 4 5 6 7 8 9.19 1 

10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98  2
8*2 + 1 = 17

101 121 123 210 212 232 234 321 323 343 345 432 434 454 456 543 545 565 567 654 656 676 678 765 767 787 789 876 878 898 987 989 3
15 * 2 + 2 = 32

29 * 2 + 3 = 61 4

0 이 나오면 1 이 되버린다. 9.19 가 나와도 1 


"""

num = 1000000000

dp =[0] * 101

dp[1] = 9

for i in range(2, n+1) :
    dp[i] = (dp[i-1]-(i-1)) * 2 + (i-1)

print(dp[n]%num)