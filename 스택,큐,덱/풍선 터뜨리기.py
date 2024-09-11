from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
q=deque([i+1,nums[i]] for i in range(n))

while q:
    k=q.popleft()
    print(k[0],end=' ')
    if k[1]>0:
        q.rotate(-(k[1]-1))
    else:
        q.rotate(-k[1])