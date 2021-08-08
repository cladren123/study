"""
문제 유형 : 위상정렬

"""
import sys
from collections import deque

input = sys.stdin.readline

# n : 과목의 수 m : 선수 조건의 수 입력
n, m = map(int, input().split())

# 선수 조건의 관계를 담을 graph
graph = [[] for _ in range(n+1)]

# 해당 과목을 듣기 위해서 몇 개의 과목을 들어야하는지를 담는 리스트
degree = [0] * (n+1)

# 선수 조건을 입력
for _ in range(m) :
    s, e = map(int, input().split())

    # 이 과목을 들으면 e를 들을 수 있는 것을 담음
    graph[s].append(e)
    
    # 이 과목을 듣기 위해선 선수과목이 몇 개 들어야 하는지를 담음
    degree[e] += 1

que = deque()

# 정답을 담을 리스트
answerlist = [0] * (n+1)

# 몇학기를 나타내는 변수 
count = 1

# 선수과목을 들을 필요가 없는 과목을 탐색하고 que에 넣는다.
for i in range(1,n+1) :
    if degree[i] == 0 :

        # 과목, 학기 순으로 담는다.
        que.append([i,count])

        # 정답리스트에 해당 과목에 들을 수 있는 학기를 담는다.
        answerlist[i] = count

# for i in graph :
#     print(i)
#
# print(degree)


while que :
    # 현재 과목과 학기를 꺼낸다.
    cur, count = que.popleft()


    for i in graph[cur] :

        # 현재 과목을 들으면 다음 수강과목의 차수를 -1 해준다.
        degree[i] -= 1

        # 선수과목의 수가 0이 되면 que에 넣어준다.
        if degree[i] == 0 :
            newcount = count + 1
            que.append([i,newcount])
            answerlist[i] = newcount


# answerlist의 값을 출력한다.
for i in range(1,n+1) :
    print(answerlist[i], end = " ")







