# 정방향을 for문을 돌려주고 
# 역방향을 for문을 돌려주어
# 문제를 푼다

n = int(input())

number = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp_reverse = [0 for i in range(n)]
dp_result = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if number[i] > number[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if number[i] > number[j] and dp_reverse[i] < dp_reverse[j]:
            dp_reverse[i] = dp_reverse[j]
    dp_reverse[i] += 1

for i in range(n):
    dp_result[i] = dp[i] + dp_reverse[i] -1

print(max(dp_result))