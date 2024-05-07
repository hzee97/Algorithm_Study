# 백준 1654 랜선 자르기
# keypoint : 이분 탐색

import sys
input=sys.stdin.readline

k,n=map(int,input().split())

lan=[]
for i in range(k):
    lan.append(int(input()))

lan.sort()

start=1
end=lan[-1]

result=0
while start<=end:
    mid=(start+end)//2
    answer=0
    for i in lan:
        answer+=i//mid
    if answer>=n:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)
