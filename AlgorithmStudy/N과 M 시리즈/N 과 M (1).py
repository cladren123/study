
"""
브루트포스 문제 대비, N과 M은 확실하게 마스터 하자.
"""


n, m = map(int, input().split())

used = [0] * m
visited = [0] * n
card = []

"""
n 은 가짓수
m 은 하나씩 뽑는다. 

입력 3 1

3개 중에서 하나 고르기 

n 개 중에서 m 개 고르기

즉 n과 m은 n개 중에서 m개 고르기. 모든 경우의 수를 고르기. 

used 는 m개 고를걸 담는다
visited 는 n개, 즉 전체에 방문하는 것을 통해 모든 경우의 수를 확인 

card는 이제 뼈대가 들어오면 생기는 몸? 같은거 덱
 
1
2
3

"""

for i in range(1, n+1) :
    card.append(i)

"""
card는 이제 뼈대가 들어오면 출력할 몸이다.
n개중에 m개 고르기

"""

def solve(stage) :
    # 종료 조건
    if stage == m :
        for i in used :
            print(card[i], end = ' ')
        print();
        return
    
    
    # visited를 이용해서 used 즉 뼈대를 만드는 작업
    for i in range(n) :
        if visited[i] == 0 :
            visited[i] = 1;
            used[stage] = i;
            solve(stage + 1);
            visited[i] = 0;



solve(0);

