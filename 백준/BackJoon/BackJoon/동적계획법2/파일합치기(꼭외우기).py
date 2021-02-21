# dp의 정의를 dp[i][j] = i번째 ~ j번째 수까지 합치는데 필요한 최소 비용이라고 하고 i <= k < j가 성립한다고 할때
# dp[i][j] = min(dp[i][k] + dp[k+1][j]) + i번째에서 j번 째 까지의 합이 성립
# https://suri78.tistory.com/15

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    page = list(map(int, input().split()))

    table = [[0]*k for _ in range(k)]
    for i in range(k-1):
        table[i][i+1] = page[i] + page[i+1]
        for j in range(i+2, k):
            table[i][j] = table[i][j-1] + page[j]

    for d in range(2, k):
        for i in range(k-d):
            j = i+d
            minimum = [table[i][k] + table[k+1][j] for k in range(i, j)]
            table[i][j] += min(minimum) 

    print(table[0][k-1])














