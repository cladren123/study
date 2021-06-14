
"""
보고 있는 채널은 100 이다.

두 가지 경우를 비교

1.
100 채널에서 +,- 버튼만 비교

2.
0<=N<=500,000 모든 경우의 수 실행
모든 채널을 순회하면서 해당 채널에서 희망채널까지 +- 버튼으로 이동했을때의 횟수

100만까지 순회하는 이유 :
큰 채널에서 작은 채널로 내려가기 위해서


"""

# 희망채널
n = int(input())

# 고장난 버튼수
m = int(input())

# 0~9 까지 버튼을 가지고 있는 리모컨 (근데 차례대로 배열되지는 않는다)
# {'2', '1', '6', '3', '8', '0', '4', '5', '7', '9'}
remote = {str(i) for i in range(10)}

# 고장난 버튼을 리모컨에서 제거
if m > 0 :
    remote -= set(map(str, input().split()))

# 현재 보고 있는 채널
channel = 100

# 현재 보고 있는 채널에서 보고자 하는 채널까지 버튼을 통해 이동했을 때 눌러야 하는 횟수
mincnt = abs(channel - n)

for cha in range(1000000) :
    # 현재 순회중인 채널의 각 자릿수 순회
    for j in range(len(str(cha))) :
        # 현재 자릿수가 누를 수 없는 버튼이라면 해당 채널은 패스
        if str(cha)[j] not in remote :
            break
        # 마지막 자릿수까지 모두 사용 가능한 버튼이라면
        elif len(str(cha)) - 1 == j :
            mincnt = min(mincnt, abs(cha-n) + len(str(cha)))

print(mincnt)


