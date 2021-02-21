# 가장 처음에 아기 상어의 크기는 2

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque

def bfs(x, y):   
    q = deque([])
    q.append([x, y])
    
    while q:       
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                fish[nx][ny] = fish[x][y] + 1
                q.append([nx, ny])

n = int(input())

fish = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n] * n
dist = [[0] * n] * n


for i in range(n):
    for j in range(n):
        if fish[i][j] == 9:
            bfs(i,j)