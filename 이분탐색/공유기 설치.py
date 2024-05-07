# 백준 2110 공유기 설치
# keypoint : 이분 탐색

import sys
input=sys.stdin.readline

n,c=map(int,input().split())

house=[]
for i in range(n):
    house.append(int(input()))

house.sort()

# start=min_gap ,end=max_gap
start=1
end=house[-1]-house[0]

result=0
while start<=end:
    mid=(start+end)//2
    tmp=house[0]
    cnt=1
    for i in range(1,n):
        if house[i]>=tmp+mid:
            tmp=house[i]
            cnt+=1

    if cnt>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1

print(result)