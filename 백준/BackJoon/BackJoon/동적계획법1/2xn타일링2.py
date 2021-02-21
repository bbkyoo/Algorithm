# 점화식 dp(n) = dp(n-1) + (2*dp(n-2)) 

n = int(input())

dp = [1,3]
if n > 1:
    for i in range(2,n):
        dp.append(dp[i-1] + (2 * dp[i-2]))

if n == 1:
    print(dp[0] % 10007)
else:
    print(dp[-1] % 10007)