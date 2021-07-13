

"""
길이에 따라 나올 수 있는 걸 전부 담아
비교하는 방법


"""


sen1 = ' ' + input()
sen2 = ' ' + input()



n = len(sen1)
m = len(sen2)

dp = [[0] * (m) for _ in range(n)]

for i in range(1,n) :
    for j in range(1,m) :
        if sen1[i] == sen2[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


# for i in dp :
#     print(i)

print(dp[-1][-1])

