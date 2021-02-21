N = int(input())
stature = list(map(int, input().split()))
ans = [0]*N

for i in range(1, N+1):
    t = stature[i-1]
    cnt = 0
    for j in range(N):
        if cnt == t and ans[j] == 0: # ans[j] == 0 이게 중복이 되지 않게 하는 제일 중요한 키 포인트
            ans[j] = i
            break
        elif ans[j] == 0:
            cnt += 1

for i in ans:
    print(i, end= " ")
