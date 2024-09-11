from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
q=deque(map(int,input().split()))
wait=deque()
k=1

while q:
    if q[0]==k:
        q.popleft()
        k+=1
    else:
        wait.append(q.popleft())

    while wait:
        if wait[-1]==k:
            wait.pop()
            k+=1
        else:
            break
            
if len(wait)==0:
    print('Nice')
else:
    print('Sad')