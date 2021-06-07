"""
문제 자체가 이해가 안감
????
아하...

제일 작은 종말의 숫자를 표시한다는거군..

1666 2666 3666 4666 5666 다음은 6666 이 아니라 6660 이다...

"""


n = int(input())
movie = 666



while n :
    if '666' in str(movie) :
        n -= 1
    movie += 1
    print(movie)

print(movie-1)



