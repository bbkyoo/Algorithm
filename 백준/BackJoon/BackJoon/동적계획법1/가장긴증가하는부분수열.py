n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]: #  배열의 다음의 숫자가 크고, 그 다음 수열의 수가 크다면 
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))