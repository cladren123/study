#문장암호화
#i love coding 이 주어지고 키워드 mask 가 주어지면, mai lsovke cmodinag 와 같이 문장 바꿀 수 있음
#문장, 키워드, 건너뛸 글자 수를 나타내는 배열 주어지면 암호문 생성 가능
#같은 방법으로 복호화
#i love coding 과  키워드 mode [0,10]이 주어지면 mi love codoing 만들 수 있음
#위의 방법대로 복호화하면 m,o를 순서대로 지워 i lve codoing이라는 결과 얻게 됨 이런 결과 나온 이유는 삽입된 키워드의 철자 대신 원래 문장의 글자 지웠기 떄문
#따라서 암호화하할때 다음 규칙 따름
#1. 키워드의 철자를 삽입하기 위해 원래 문장을 건너띄는 도중, 방금 건너뛴 글자와 이번에 삽입할 키워드의
# 철자가 같은 경우 건너띄는 것을 중단하고 그 위치에 키워드의 철자 삽입
#2. 위 예시의 경우 0번 건나뛴 위치에 m을 삽입한 뒤 다음 철자 o을 상빙하기 위해 10번 건너띄는 도중 love에서 o을
# 발견하고 lo 뒤에 o를 삽입=> mi loove coding으로 암호화됨 키워드의 철자를 삽입한 횟수가 2이므로
# 왼쪽에서부터 첫 번쨰 m과 o을 지우면 원래 문장을 얻을 수 있음
#10<=sentence<=1,000,000
#2<=keyword<=20
#1<=skips 길이<=1,000,000
#0<=skips원소<=10
# 입출력1
# sentence = i love coding
# keyword = mask
# skips = [0,0,3,2,3,4]
# result = mai lsovke cmodinag
# 입출력2
# i love coding
# keyword = mode
# skips = [0, 10]
# result = mi loove coding
# 입출력3
# sentence = abcde fghi
# keyword = xyz
# skips = [10,0,1]
# result = abcde fghixy

def solution(sentence, keyword, skips):
    answer = ''
    n = 0
    while skips[n] != 0:
        answer = keyword[skips[n]] + sentence
        n+=1
    print(answer)
    for i in range(len(sentence)):
        ''

    return answer