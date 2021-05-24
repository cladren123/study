"""
2846번 오르막길

"""

n = int(input())
height = list(map(int, input().split()))
height.append(0)

check1 = 0
check2 = 0
result = []

for i in range(n) :
    if height[i] < height[i+1] :
        check2 += 1
    else :
        result.append(height[check2] - height[check1])
        check1 = i+1
        check2 = i+1

print(max(result))




