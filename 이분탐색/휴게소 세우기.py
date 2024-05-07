# 백준 1477 휴게소 세우기
# keypoint : 이분탐색

import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
info=list(map(int,input().split()))

info.append(0)
info.append(l)
info.sort()

start=1
end=l

answer=0
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in range(1,len(info)):
        if info[i]-info[i-1]>mid:
            cnt+=(info[i]-info[i-1]-1)//mid

    if cnt>m:
        start=mid+1
    else:
        end=mid-1
        answer=mid

print(answer)