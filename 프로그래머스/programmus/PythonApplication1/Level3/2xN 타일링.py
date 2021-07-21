def solution(n):
    dp = [1]+[0]*n
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007 # 이거 % 1000000007 를 여기에 넣으면 시간이 더 줄어듬

    return dp[n]
