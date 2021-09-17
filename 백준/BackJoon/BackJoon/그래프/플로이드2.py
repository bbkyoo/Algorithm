import sys

n = int(input())
m = int(input())
inf = sys.maxsize

dp = [[inf]*(n+1) for _ in range(n+1)]
prev = [[None]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if dp[a][b] > c:
        dp[a][b] = c
        prev[a][b] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                prev[i][j] = prev[k][j]

for i in dp[1:]:
    tmp = []
    for j in i[1:]:
        if j == inf:
            tmp.append(0)
        else:
            tmp.append(j)
    print(*tmp)

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == inf:
            print(0)
        else:
            route = [j]
            tmp = j
            while tmp != i:
                route.append(prev[i][tmp])
                tmp = prev[i][tmp]

            print(len(route), end='')
            print(*route[::-1])