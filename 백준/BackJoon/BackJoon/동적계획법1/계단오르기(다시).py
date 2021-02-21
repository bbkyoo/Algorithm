# 가장 중요한 것은 마지막 계단의 전을 밟았는가
# 마지막 계단의 전을 밟지x
# 이 것을 하기 전에 먼저 n = 1 , 2, 3, 4 일때 등등을 생각하고
# 규칙이 구해지는 때부터 점화식을 사용해서 푼다

n = int(input())

s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])

print(dp[n - 1])



























