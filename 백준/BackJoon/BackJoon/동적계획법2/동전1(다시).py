#1. n가지 종류의 동전을 반복문으로 순회하면서 내부에서 반복문을 한 차례 더 돌린다.
#2. 이 때 내부 반복문은 동전의 가치부터 k까지 순회한다.
#3. 내부 반복문이 j번째를 순회한다고 했을 때 dp[j]에 dp[j-(순회중인 동전의 가치)]의 값을 더해준다.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())

coin = []

for _ in range(n):
    x = int(input())
    coin.append(x)

dp = [0 for i in range(10001)]
dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])
