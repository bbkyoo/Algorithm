import sys

sys.setrecursionlimit(50000) #재귀제한높이설정(기본값이상으로 안해주면 런타임에러)

input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y,c):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny, c)
        
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
   
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    
    count = 0
    
    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1 and visited[a][b] == 0:
                dfs(a,b,count)
                count += 1

    print(count)