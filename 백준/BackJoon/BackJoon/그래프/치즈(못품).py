# https://it-garden.tistory.com/274

from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque([])
    q.append([0,0])
    ch = [[-1]*m for _ in range(n)]
    ch[0][0] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if ch[nx][ny] == -1:
                    if matrix[nx][ny] >= 1:
                        matrix[nx][ny] += 1
                    else:
                        ch[nx][ny] = 0
                        q.append([nx, ny])

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
c = 0

while True:
    bfs()
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] >= 3:
                matrix[i][j] = 0
                cnt = 1
            elif matrix[i][j] == 2:
                matrix[i][j] = 1

    if cnt == 1:
        c += 1
    else:
        break

print(c)