"""
알파벳 26
A B C D
0 1 2 3
4 3 2 1

A : 65
Z : 90
M : 77
N : 78

A -> M : 12
Z -> M : 13

A -> N : 13
Z -> N : 12

즉, 77이하면 A에서 가는게 빠르고 78 이상이면 Z에서 가는게 빠르다.

"ABAAAAAAAAABB", 7
바꿀 때마다 시행해야하나..

"JAZ", 11

"""


# name = "JEROEN"
# name = "JAN"
name = "ABBAAAAAAAAAB"
# name = "JAZ"

def solution(name):
    answer = 0
    newname = list(name)
    n = len(name)

    visited1 = [0] * n
    visited1[0] = 1

    for i in range(n) :
        # print(newname[i])
        if newname[i] == 'A' :
            visited1[i] = 1
        if newname[i] <= 'M' :
            ans =  ord(newname[i]) - ord('A')
            answer += ans
            # print('s', ans)
        else :
            ans = ord('Z') - ord(newname[i]) + 1
            answer += ans
            # print('l', ans)

    # print(answer)

    print(visited1)

    leftstart = 0
    rightstart = 0

    guri = 0

    while True :
        if 0 not in visited1 :
            break;

        left = 0
        right = 0

        while visited1[leftstart] != 0 :
            leftstart -= 1
            if leftstart < 0 :
                leftstart = n - 1
            left += 1
        while visited1[rightstart] != 0 :
            rightstart += 1
            if rightstart > n-1 :
                rightstart = 0
            right += 1

        anv = min(left,right)

        if anv == right :
            leftstart = rightstart
            visited1[rightstart] = 1
        else :
            rightstart = leftstart
            visited1[leftstart] = 1
        guri += anv

    print(guri)
    answer += guri
    print(answer)

    return answer

solution(name)

"""
다른 사람의 풀이 
def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0:
            break
        left, right = 1, 1
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer

"""