# keypoint : 이분탐색, 두 포인터

import sys
input=sys.stdin.readline

n=int(input())
info=list(map(int,input().split())) # 이미 정렬된 순서로 주어짐.

start=0
end=n-1
val=sys.maxsize   # 기준값

result1=0
result2=0
while start<end:
    mix=info[start]+info[end]

    if abs(mix)<val:
        val=abs(mix)
        result1=info[start]
        result2=info[end]

    if mix<0:
        start+=1
    elif mix>0:
        end-=1
    else:
        break

print(result1,result2)