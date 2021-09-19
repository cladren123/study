
citations =[0,1,1]

def solution(citations):
    citations.sort(reverse=True)
    print(citations)

    n = len(citations)

    for i in range(n):
        print(i, end=" ")
        if i >= citations[i]:
            answer = i
            break

    return answer

def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
    return 0



# 테스트케이스 9.19 실패...
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n) :
        if i >= citations[i] :
            answer = i
            break
    return answer
