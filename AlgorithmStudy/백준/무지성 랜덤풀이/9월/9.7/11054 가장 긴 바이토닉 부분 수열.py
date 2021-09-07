
"""

문제 유형 : DP

dp를 2개 만들어서 오름수열, 내림수열을 구해 더해서 가장 큰 값을 구한다.

"""

n = int(input())
nl = list(map(int, input().split()))




dp1 = [1] * n

# 오름차순 가장 큰 것

for i in range(n) :
    for j in range(i) :
        if nl[i] > nl[j] :
            dp1[i] = max(dp1[i], dp1[j] + 1)

# print(dp1)

# 내림차순 가장 큰 것
# 시작하는 위치가 바뀌므로 다 구해줘야 한다.



for k in range(n) :
    dp2 = [0] * n
    for i in range(k,n) :
        for j in range(k,i) :
            if nl[i] < nl[j] :
                dp2[i] = max(dp2[i], dp2[j] + 1)
    dp1[k] += max(dp2)

# print(dp1)
print(max(dp1))























