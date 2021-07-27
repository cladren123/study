import sys

input = sys.stdin.readline
n,s = map(int, input().split())
nlist = list(map(int, input().split()))

start = 0
end = 1

check = nlist[start] + nlist[end]
answer = sys.maxsize

while True :

    if check >= s :
        # print(start,end)
        answer = min(answer, end-start+1)
        check -= nlist[start]
        start += 1

    else :
        end += 1
        # 끝까지 다 더했을 때 부분합을 못넘었으면 뭔 짓을 해도 구할 수 없으니 끝내야 한다.
        if end == n :
            break
        check += nlist[end]


if sum(nlist) < s :
    answer = 0

print(answer)
