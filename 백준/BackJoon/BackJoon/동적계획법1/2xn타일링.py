n = int(input())

sqare = [1]
dp = [1,1]

if n > 1:
    for i in range(1,n):
        dp.append(sqare[i-1] + dp[i])
        sqare.append(dp[i])

print(dp[-1] % 10007)
