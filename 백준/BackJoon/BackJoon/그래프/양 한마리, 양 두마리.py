from collections import deque

def bfs(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([])
    q.append([x, y])
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == 0 and matrix[nx][ny] == '#':
                    q.append([nx, ny])
                    visited[nx][ny] = 1

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    matrix = []
    visited = [[0]*w for _ in range(h)]

    for _ in range(h):
        matrix.append(list(input()))
    
    result = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '#' and visited[i][j] == 0:
                bfs(i, j)
                result += 1

    print(result)




