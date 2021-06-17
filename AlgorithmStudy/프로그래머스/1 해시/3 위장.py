
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(clothes):

    # print(clothes)

    camo = dict()

    for product,clothtype in clothes :
        if clothtype in camo :
            camo[clothtype].append(product)
        # list 형식으로 넣어주어야 append 함수를 쓸 수 있다.
        else :
            camo[clothtype] = [product]

    print(camo)

    list1 = []

    for i in camo :
        list1.append(len(camo.get(i))+1)
        print(list1)
    answer = 1
    for i in list1 :
        answer = answer * i

    answer -= 1
    return answer

print(solution(clothes))