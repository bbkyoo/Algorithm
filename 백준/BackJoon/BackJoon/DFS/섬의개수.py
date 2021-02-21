# 지도의 너비 w와 높이 h
import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    dx = [1,-1,0,0,1,-1,1,-1] # 상하좌우 대각선까지 고려
    dy = [0,0,-1,1,-1,-1,1,1] # 상하좌우 대각선까지 고려
    
    visited[x][y] = 1
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]        
        if 0 <= nx < h and 0 <= ny < w: 
            if visited[nx][ny] == 0 and ireland[nx][ny] == 1:               
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    ireland = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)] # 이거 꼭 이렇게 써라
    num = 0

    for i in range(h):
        for j in range(w):
            if ireland[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                num += 1
    print(num)