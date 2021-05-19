# 1.
#
# 입출력 예
# #1
# p는 2 이상 10 이하의 자연수입니다.
# index는 1 이상 10,000 이하의 자연수입니다.
# p=10 이므로 10진법을 사용합니다.
# 종이에는 "0123456789101112131415..." 가 써지게 됩니다.
# index=15 이므로 15번째 글자인 1을 return 하면 됩니다.
#
# #2
# p=6 이므로 6진법을 사용합니다.
# 종이에는 "01234510111213141520212223..." 가 써지게 됩니다.
# index=20 이므로 20번째 글자인 0을 return 하면 됩니다.
#
# #3
# p=2 이므로 2진법을 사용합니다.
# 종이에는 "01101110010111011110001001..." 가 써지게 됩니다.
# index=16 이므로 16번째 글자인 1을 return 하면 됩니다.

######################################################################################################################
def makePNum(num, p):
    mok = num; temp = "";                                           # 몫에는 가장 큰 값인 num으로 초기화
    if num < p:                                                     # num이 피제수보다 작으면 num을 str로 바꿔 리턴
        return str(num);
    while mok >= p:                                                 # 몫이 피제수보다 큰 값일 동안
        mok = num // p;                                             # num을 p로 나눠 몫과 나머지를 구해
        nmg = num % p;
        num = mok;
        temp = str(nmg) + temp;                                     # 나머지를 반복해서 str의 맨 앞으로 삽입
        if mok < p:                                                 # 몫이 피제수보다 작은 경우가 마지막 이므로 몫을 str 맨 앞에 삽입
            temp = str(mok) + temp;
    return temp;

num, index, p = map(int, input("num, index, p 입력: ").split());

temp = "";
for i in range(num + 1):                                            # 0부터 num까지 p진법으로 변환한 수를 str로 만들어 더한다
    retData = makePNum(i, p);
    temp = temp + retData;

# temp = makePNum(num, p);
print(temp);                                                        # str의 index번째 수를 출력한다
print(temp[index - 1]);