n = int(input())

arr = []
max_l = 0
max_h = 1
max_index = 0

for _ in range(n):
    l, h = map(int, input().split())
    arr.append([l, h])
    if max_l < l:
        max_l = l
    if max_h < h:
        max_h = h
        max_index = l 

dp = [0] * (max_l + 1)
for l, h in arr:
    dp[l] = h

total = 0
temp = 0
for i in range(max_index + 1):
    if dp[i] > temp:
        temp = dp[i]
    total += temp

temp = 0
for i in range(max_l, max_index, -1):
    if dp[i] > temp:
        temp = dp[i]
    total += temp

print(total)




