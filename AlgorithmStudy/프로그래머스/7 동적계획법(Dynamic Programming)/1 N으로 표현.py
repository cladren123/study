
N = 5
number = 12

# N = 5
# number = 31168

def solution(N, number) :
    s = [0, {N}]

    if N == number :
        return 1

    for i in range(2,9) :
        # N의 자릿수 추가
        case_set = {int(str(N)*i)}
        # i의 절반만 돈다.
        # i = 4
        # i_half = 1,2
        for i_half in range(1, i//2+1) :
            for x in s[i_half] :
                # i - i_half = 3,2
                for y in s[i - i_half] :
                    # 즉 12 랑 34를 비교하게 된다.
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if x != 0 :
                        case_set.add(y/x)
                    if y != 0 :
                        case_set.add(x/y)
        if number in case_set :
            return i
        s.append(case_set)
    return -1






print(solution(N, number))
