
"""
https://claude-u.tistory.com/449

이분탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아낸다.
A보다 작은 숫자가 몇개인지 알면 A가 몇 번째 숫자인지 알 수 있다.

예) 10 * 10 에서 20보다 작거난 같은 수
1*1 ~ 1*10
2*1 ~ 2*10
3*1 ~ 3*6
...
10*1 ~ 10*2

이런 숫가 나오는데 이는 반대로 생각하면 20을 행으로 나눈 몫이다.

20 // 1 : 10개
20 // 2 : 10개
20 // 3 : 6개
...
20 // 10 : 2개

이 성질을 이용하자

temp = 0
for i in range(1,n+1) :
    temp += min(mid//i,n)

해당 숫자(mid) 보다 작거나 같은 숫자들을 전부 찾아줌으로써 mid가 몇번째 위치한 숫자인지
알아낼 수 있다.

이를 이분탐색으로 진행한다.



"""

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, k

while start <= end :
    mid = (start + end) // 2

    # mid가 몇 번째 숫자인지 구한다. temp
    temp = 0
    for i in range(1, n+1) :
        temp += min(mid//i, n)

    # temp가 k 보다 크면 end를 미드로 땡겨서 mid의 크기를 낮춘다.
    if temp >= k :
        answer = mid
        end = mid - 1
    # temp가 k보다 작으면 start를 mid로 땡겨서 mid의 크기를 높힌다.
    else :
        start = mid + 1

    # 이렇게 땡기기를 반복해서 temp가 더 이상 땡길 수 없는 k랑 같아질 때 답이 된다.


print(answer)




















