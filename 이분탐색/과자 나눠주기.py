# 백준 16401 과자 나눠주기
# keypoint : 이분 탐색

import sys
input=sys.stdin.readline

m,n=map(int,input().split())
snack=list(map(int,input().split()))

snack.sort()

if m>sum(snack):
    print(0)
else:
    start=1
    end=snack[-1]
    result=0
    while start<=end:
        mid=(start+end)//2
        answer=0
        for i in snack:
            answer+=i//mid
        if answer>=m:
            result=mid
            start=mid+1
        else:
            end=mid-1
    print(result)