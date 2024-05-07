# 백준 3079 입국심사
# keypoint : 이분 탐색

n,m=map(int,input().split())

times=[]
for i in range(n):
    times.append(int(input()))

times.sort()

start = min(times)
end = max(times)*m

answer=0
while start <= end:
    mid = (start + end) // 2
    people = 0
    for i in times:
        people += mid // i
        if people >= m:
            break
    if people < m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)