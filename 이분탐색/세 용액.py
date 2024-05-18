# 백준 2473 세 용액
# keypoint : 이분탐색, 두 포인터

import sys
input=sys.stdin.readline

n=int(input())
info=list(map(int,input().split()))

info.sort()  # 정렬

val=sys.maxsize   # 기준값

result=[]
for i in range(n-2):
    start=i+1
    end=n-1
    while start<end:
        mix=info[i]+info[start]+info[end]
        if abs(mix)<val:
            val=abs(mix)
            result=[info[i],info[start],info[end]]

        if mix<0:
            start+=1
        elif mix>0:
            end-=1
        else:
            break

print(*result)