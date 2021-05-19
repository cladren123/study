"""
상담을 완료하는데 걸리는 기간 Ti
상담을 했을 때 받을 수 있는 금액 Pi

최대 이익을 출력하자.
"""

n = int(input())

ti = [0]
pi = [0]
dp = [0]

for i in range(n) :
    days, money = map(int, input().split())
    ti.append(days)
    pi.append(money)
    dp.append(money)

dp.append(0)
# print(ti)
# print(pi)
# print(dp)


for i in range(n, -1, -1) :
    if ti[i] + i - 1 > n :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1], pi[i] + dp[i+ti[i]])

# print(dp)
print(dp[0])

"""
피드백
이번 DP는 그전에 풀었던 것과는 달랐다. 
3개 연속못한다 해서 점화식을 찾았지만
이번 디피는 조건이 제각각 이었기 때문에 뒤쪽에서부터 값을 더했다.
DP에도 다양한 경우가 있다는 것을 알았고
조건이 제각각인 경우에는 뒤에서부터 구하는 방법을 생각해야겠다. 
"""



