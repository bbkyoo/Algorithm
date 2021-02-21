n, m = map(int, input().split())

arr = [input() for _ in range(n)]

k = int(input())

cnt = [0]*n

if k % 2: # 만약 k가 홀수 라면
    for i in range(n):
        zero_cnt = arr[i].count('0')
        if zero_cnt % 2 and zero_cnt <= k: # 0의 수가 홀수 이고 0의 갯수가 k랑 같거나 작다면
            for j in range(n):
                if arr[i] == arr[j]: # 불의 상태가 같은것을 찾는다 
                    cnt[i] += 1

else: # 만약 k가 짝수 라면 
    for i in range(n):
        zero_cnt = arr[i].count('0')
        if not zero_cnt % 2 and zero_cnt <= k: # 0의 수가 짝수 이고 0의 갯수가 k랑 같거나 작다면
            for j in range(n):
                if arr[i] == arr[j]: # 불의 상태가 같은것을 찾는다 
                    cnt[i] += 1

print(max(cnt))