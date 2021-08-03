"""
문제 분류 : DP
"""
import sys

input = sys.stdin.readline

# n : 물품의 수 k : 버틸 수 있는 무게
n, k = map(int, input().split())

nlist = []

for i in range(1,n+1) :
    # w : 물건의 무게, v : 물건의 가치
    w, v = map(int, input().split())
    nlist.append([w,v])

nlist.sort()
# print(nlist)

weightsum = 0
valuesum = 0

maxvalue = 0

start = 0
end = 0

while True :
    weightsum += nlist[end][0]

    if weightsum <= k :
        valuesum += nlist[end][1]
        maxvalue = max(maxvalue, valuesum)

        end += 1

        if end == n :
            break

    elif weightsum > k :
        start += 1
        end = start

        weightsum = 0
        valuesum = 0


print(maxvalue)
















