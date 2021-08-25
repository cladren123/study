
"""

예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	"z--"
예3	"=.="	"aaa"
예4	"123_.def"	"123_.def"
예5	"abcdefghijklmn.p"	"abcdefghijklmn"

"""



def solution(new_id):
    answer = ''

    one1 = new_id.lower()

    # print(one1)

    characters = "abcdefghijklmnopqrstuvwxyz0123456789-_."

    one2 = ""

    for i in one1 :
        if i in characters :
            one2 += i

    # print(one2)

    one3 = one2.replace("..", ".")

    # print(one3)

    while(".." in one3) :
        one3 = one3.replace("..", ".")

    # print(one3)

    if len(one3) >= 1 :
        if one3[0] == "." :
            one3 = one3[1:]

    if len(one3) >= 1:
        if one3[-1] == "." :
            one3 = one3[:-1]


    if len(one3) == 0 :
        one3 += "a"

    # print(one3)

    # 6단계

    if len(one3) >= 16 :
        one3 = one3[:15]

    if one3[-1] == "." :
        one3 = one3[:-1]

    # print(one3)

    # 7단계

    while len(one3) <= 2 :
        one3 += one3[-1]

    print(one3)

    answer = one3



    return answer


solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")


