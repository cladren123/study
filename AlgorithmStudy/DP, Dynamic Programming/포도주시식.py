
# 연속해서 3잔을 마실 수 없다.

n = int(input())

drink = [0]

for i in range(n) :
    podo = int(input())
    drink.append(podo)

dp = [0]
dp.append(drink[1])

if n > 1 :
    dp.append(drink[1] + drink[2])

for i in range(3, n+1) :
    dp.append(max(dp[i-1], dp[i-3] + drink[i-1] + drink[i], dp[i-2] + drink[i]))
print(dp[n])

"""
dp에는 그 순간에 가장 많이 마실 수 있는 경우만 저장한다!
경우의 수를 구한 최대값을 저장해 나가면서 DP의 배열을 채워나간다. 




"""
