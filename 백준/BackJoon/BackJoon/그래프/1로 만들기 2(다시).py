n = int(input())
dp = [[0,[]] for _ in range(n+1)]

# 초기화
dp[1][0]=0
dp[1][1]=[1]

for i in range(2, n+1):
    # 1을 뺄때
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]

    # 2로 나누어 떨어질때
    if i%2==0 and dp[i][0] > dp[i//2][0] + 1:
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]
    
    # 3으로 나누어 떨어질때
    if i%3==0 and dp[i][0] > dp[i//3][0] + 1:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]

print(dp[n][0])
dp[n][1].reverse()

for i in dp[n][1]:
    print(i, end= " ")



























