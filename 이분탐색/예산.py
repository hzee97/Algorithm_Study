# 백준 2512 예산
# keypoint : 이분 탐색

import sys
input=sys.stdin.readline

n=int(input())
req=list(map(int,input().split()))
m=int(input())

req.sort()

if sum(req)<=m:
    print(max(req))
else:
    start=0
    end=req[-1]
    result=0
    while start<=end:
        mid=(start+end)//2
        answer=0
        for i in req:
            if i<=mid:
                answer+=i
            else:
                answer+=mid
        if answer>m:
            end=mid-1
        else:
            result=mid
            start=mid+1
    print(result)