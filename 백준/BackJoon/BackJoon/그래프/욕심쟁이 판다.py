import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if s[x][y] < s[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

n = int(input())

s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

dp = [[0]*n for i in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)


