import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())

lesson=list(map(int,input().split()))
# print(lesson)
l=max(lesson)
r=sum(lesson)
ans=sys.maxsize
while l<=r:
    mid=(l+r)//2
    cnt=0
    sum=0
    for i in range(len(lesson)):
        if sum+lesson[i]>mid:
            cnt+=1
            sum=0
        sum+=lesson[i]
    if sum:
        cnt+=1

    if cnt>m: # 블루레이 개수가 m보다 커 (각 크기가 작음)
        l=mid+1
    else:
        ans=min(ans,mid)
        r=mid-1
print(ans)