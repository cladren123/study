
# N = 5
# number = 12

N = 5
number = 31168

def solution(N, number) :
    answer = 0

    if N == number :
        return 1

    dp = [[] for _ in range(9)]

    for i in range(1,9) :
        strn = str(N)

        newnum = strn * i
        dp[i].append(int(newnum))
        dp[2].append(N)
        # print(dp[i])

        if number in dp[i] :
            answer = i
            print(answer)
            return answer

        if i == 8 :
            answer = -1
            print(answer)
            return answer

        for j in dp[i] :
            for k in dp[i] :
                dp[i+1].append(j+k)
                dp[i+1].append(j*k)
                dp[i+1].append(abs(j-k))
                if k == 0 :
                    continue
                dp[i+1].append(int(j/k))

        newdp = set(dp[i+1])
        dp[i+1] = list(newdp)


    print(answer)
    return answer

solution(N, number)
