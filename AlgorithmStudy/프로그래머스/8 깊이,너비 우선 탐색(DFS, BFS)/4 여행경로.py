from collections import deque
from copy import deepcopy

"""
T 1 : [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
ans : ["ICN", "B", "ICN", "A", "D", "A"]

T 2: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
ans : ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

T 3 : [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
ans : ["ICN", "COO", "ICN", "BOO", "DOO"]

4번 반례 해결하니 2번 테케 통과했습니다.
T 4: [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
ans : ["ICN", "SFO", "ICN", "SFO", "QRE"]

가장 골치아픈 1번테케는 5번반례 해결후 통과했습니다.
T 5 : [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
ans : ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
"""



# 2번 테스트케이스
# [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]


tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]

def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for start, end in tickets :
        if start in routes :
            routes[start].append(end)
        else :
            routes[start] = [end]
    # 시작 지점 인천에서 스타뜨!
    st = ['ICN']
    answer = []
    while st :
        # st 에서 맨 마지막 것을 꺼낸다.
        top = st[-1]
        # routes에 top이 없거나 top의 길이가 0일 때
        # 경로를 없애면 어쩔 수 없이 정답에 들어간다
        # top 은 st -1 을 가저오니 마지막에 ICN이 남는다. 즉 역순으로 순서를 쌓이게 된다.
        
        print(st)
        # 더 갈길이 없다. 마지막. 제일 끝.
        if top not in routes or len(routes[top]) == 0 :
            answer.append(st.pop())
        else :
            st.append(routes[top].pop())
    answer.reverse()
    return answer

print(solution(tickets))
