

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = "zceec"

def isPalindrome(s) :
    answer = True

    s = s.lower()
    # print(s)

    news = []

    for i in s :
        if 'a' <= i <= 'z' or '0' <= i <= '9.19' :
            news.append(i)

    print(news)

    for i in range(int(len(news)/2)) :
        if news[i] != news[-(i+1)] :
            answer = False
    print(answer)
    return answer

isPalindrome(s)

