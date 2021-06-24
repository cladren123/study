
# s = "aba"
# s = "abca"
s = "abc"
# s = "zceecq"
# s = "yd"

def validPalindrome(s) :
    answer = False
    check = 1
    checker = 0

    s = list(s)
    ban = int(len(s)/2)

    for i in range(len(s)) :
        news = s.copy()
        del news[i]
        ban2 = int(len(news) / 2)
        # print(news)
        for j in range(ban2) :
            # print(news[j], news[-(j+1)])
            if news[j] == news[-(j+1)] :
                checker += 1
        # print(checker, ban2)
        if checker == ban2 :
            answer = True
            break
        checker = 0



    print(answer)
    return answer

validPalindrome(s)