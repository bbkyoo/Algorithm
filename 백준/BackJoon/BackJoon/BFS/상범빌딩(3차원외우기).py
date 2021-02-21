from collections import deque
import sys

input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    q = deque()
    q.append([sz, sy, sx])
    visited[sz][sy][sx] = 1

    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nx = x + dx[i] 
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and visited[nz][ny][nx] == 0:
                if matrix[nz][ny][nx] == '.' or matrix[nz][ny][nx] == 'E':
                    dp[nz][ny][nx] = dp[z][y][x] + 1
                    visited[nz][ny][nx] = 1
                    q.append([nz, ny, nx])

while True:
    l, r, c = map(int, input().split()) 

    if l == 0:
        break

    matrix  = [[]*r for i in range(l)]
    dp = [[[0]*c for i in range(r)] for i in range(l)]
    visited = [[[0]*c for i in range(r)] for i in range(l)]

    for i in range(l):
        for j in range(r):
            matrix[i].append(list(map(str, input())))
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if matrix[i][j][k] == 'S':
                    sx, sy, sz = k, j, i
                elif matrix[i][j][k] == 'E':
                    ex, ey, ez = k, j, i 

    bfs()
    if dp[ez][ey][ex] == 0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % dp[ez][ey][ex])















