from collections import deque

def bfs():
    global k
    q = deque([])
    q.append([0,0,k])
    visited = [[[0 for i in range(31)] for i in range(w)] for _ in range(h)]
    
    while q:
        x, y, z = q.popleft()

        if x == h-1 and y == w-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny][z] == 0 and matrix[nx][ny] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])

        if z > 0:
            for i in range(8):
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if matrix[nx][ny] == 0 and visited[nx][ny][z-1] == 0:
                        visited[nx][ny][z-1] = visited[x][y][z] + 1
                        q.append([nx, ny, z-1])

    return -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
dx2 = [2,-2,1,-1,2,-2,1,-1]
dy2 = [-1,-1,-2,-2,1,1,2,2]

k = int(input())
w, h = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]
print(bfs())

