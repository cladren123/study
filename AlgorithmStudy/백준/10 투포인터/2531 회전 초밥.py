import sys

input = sys.stdin.readline


# n : 접시의 수
# d : 초밥의 가짓수
# k : 연속해서 먹는 접시의 수
# c : 쿠폰 번호

n, d, k, c = map(int, input().split())

cho = []

for _ in range(n) :
    cho.append(int(input()))

check = set()
answerlist = []

for p1 in range(n) :
    for p2 in range(p1, p1+k) :
        if p2 > n-1 :
            p2 = p2 - (n)
        check.add(cho[p2])
    check.add(c)
    # print(check)
    answerlist.append(len(check))
    check.clear()

print(max(answerlist))

