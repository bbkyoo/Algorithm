def solution(n, money):
    dp = [1] + [0]*n

    for i in money:
        for j in range(i, n+1):
            if j >= i:
                dp[j] += dp[j-i]

    return dp[n] % 1000000007

n = 5
money = [1,2,5]
print(solution(n, money))