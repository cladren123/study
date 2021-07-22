import sys

input = sys.stdin.readline

N,H = map(int, input().split())

highlist = []
lowlist = []

for i in range(N) :
    obone = int(input())
    if i % 2 == 0 :
        lowlist.append(obone)
    else :
        highlist.append(obone)

lowlist.sort()
highlist.sort()

answer = sys.maxsize
answercount = 0

def check(height, cave) :
    start = 0
    end = len(cave) - 1

    while start <= end :
        mid = (start + end) // 2
        if cave[mid] <= height :
            start = mid + 1
        else :
            end = mid - 1

    return len(cave) - (end+1)


for i in range(1, H+1) :
    lowcount = check(i-1, lowlist)
    highcount = check(H - i, highlist)

    curcount = lowcount + highcount

    if curcount < answer :
        answer = curcount
        answercount = 1
    elif curcount == answer :
        answercount += 1
    else :
        pass

print(answer, answercount)


