# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9CDP

def solution(n, money):
    dp = [1] + [0]*n

    for i in money:
        for j in range(i, n+1):
            if j >= i:
                dp[j] += dp[j-i]

    return dp[n] % 1000000007
