# https://sungmin-joo.tistory.com/21
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

if n == 1:
    print(dp[1])
elif n == 2:
    print(dp[2])
else:
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    print(dp[n])


