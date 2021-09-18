"""

문제유형 :
브루트포스
백트랙킹

|a[0] - a[1]| + |a[1] - a[2]| .. + |a[n-2] - a[n-1]|
위의 식에 최댓값을 구하는 프로그램 작성

경우의 수를 모든 구한 다음에 대입하자.

"""
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 문제에 주어진 식을 계산해 답을 return 하는 함수
def cal(alist) :
    global n
    answer = 0

    for i in range(n-1) :
        one = abs(alist[i] - alist[i+1])
        answer += one

    return answer

# 경우의 수를 구한자.
achoose = list(permutations(a, n))

answer = -sys.maxsize
for one in achoose :
    check = cal(one)
    answer = max(answer, check)

print(answer)

