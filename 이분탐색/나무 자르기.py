# 백준 2805 나무 자르기
# keypoint : 이분 탐색

import sys
input=sys.stdin.readline

n,m=map(int,input().split())    # n : 나무의 수, m : 나무의 길이
h=list(map(int,input().split()))  # 나무의 높이들

h.sort()

start=0
end=h[-1]

result=0
while start<=end:
    mid=(start+end)//2
    answer=0
    for i in h:
        if i>mid:
            answer+=i-mid
    if answer>=m:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)