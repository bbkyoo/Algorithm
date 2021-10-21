h, w = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]*w

mx_val =0
mx_idx =0

for i in range(len(arr)):
    if arr[i] > mx_val:
        mx_val = arr[i]
        mx_idx = i

temp = 0
for i in range(mx_idx):    
    if temp < arr[i]:
        temp = arr[i]
        dp[i] = temp
    else:
        dp[i] = temp

temp = 0
for i in range(w-1, mx_idx, -1):    
    if temp < arr[i]:
        temp = arr[i]
        dp[i] = temp
    else:
        dp[i] = temp

dp[mx_idx] = mx_val
answer = 0
for i in range(w):
    answer += dp[i] - arr[i]

print(answer)