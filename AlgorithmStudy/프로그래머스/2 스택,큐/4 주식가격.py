
prices = [1,2,3,2,3]

def solution(prices) :
    answer = []

    prices.append(0)

    list1 = [0] * 100000

    n = len(prices)
    list2 = []

    # print(n)

    for i in range(n) :
        for j in range(0,i+1) :
            # print(j)
            if i+1 <= n :
                if prices[i] >= prices[j] :
                    if j not in list2 :
                        list1[j] += 1
                else :
                    list2.append(j)


            # print(prices[i], prices[j])
            # print(list1)


    # print(list1)
    answer = list1[0:n-1]
    print(answer)






    return answer



solution(prices)