from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,-1,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 0:
                    q.append([nx, ny])





n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)] 
