import sys
sys.setrecursionlimit(10**5)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and region[nx][ny] > v:
            dfs(nx, ny)

n = int(input())

r_mx = 0

region = []
for _ in range(n):
    line = list(map(int, input().split()))
    r_mx = max(r_mx, max(line))
    region.append(line)

v = 0
mx = 0
while v <= r_mx:
    num = 0
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if region[i][j] > v and visited[i][j] == 0:
                dfs(i,j)
                num += 1            
    mx = max(mx, num)
    v += 1      
print(mx)    