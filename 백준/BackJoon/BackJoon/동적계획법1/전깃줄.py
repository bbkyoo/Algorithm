n = int(input())

electronic = []
 
for i in range(n):
    x, y = map(int, input().split())
    electronic.append([x,y])

electronic = sorted(electronic, key = lambda x : x[0])

dp = [0] * n
dp[0] = 1

for i in range(1,n):
    min_value = 0
    for j in range(i):
        if(electronic[i][1] > electronic[j][1]):
            min_value = max(dp[j], min_value)
    dp[i] = min_value + 1

print(n - max(dp))

