"""
테스트케이스
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)


"""



from collections import deque


def solution(begin, target, words) :
    # print(begin, target, words)
    answer = 0

    if target not in words :
        answer = 0
    else :
        m = len(words)
        n = len(begin)
        que = deque()
        que.append([begin, 0])
        while que :
            # print(que)
            start, number = que.popleft()

            if number > m :
                answer = 0
                break

            if start == target :
                answer = number
                break

            for wordone in words :
                count = 0
                for j in range(n) :
                    if start[j] == wordone[j] :
                        count += 1
                if count == n-1 :
                    newnumber = number + 1
                    que.append([wordone, newnumber])


    print(answer)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"])) # 1
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"])) # 3
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"])) # 4



solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])