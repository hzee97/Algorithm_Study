# 백준 2295 세 수의 합
# keypoint : 구현

import sys
input=sys.stdin.readline

n=int(input())

u=[]
for i in range(n):
    u.append(int(input()))

u.sort()

case=set()
for i in u:
    for j in u:
        case.add(i+j)

for i in range(n-1,-1,-1):
    for j in range(i+1):
        if u[i]-u[j] in case:
            print(u[i])
            exit()
