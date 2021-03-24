from collections import deque

n, m = map(int, input().split())

dx = [0,-1,0,1]
dy = [1,0,-1,0] # 북 서 남 동

def bfs(b_a, b_b):
    q = deque([])
    q.append((b_a,b_b))
    visited[b_a][b_b] = 1
    dist[b_a][b_b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if i == 0 or i == 2:
                if 0 <= nx < m and 0 <= ny < n:
                    if visited[nx][ny] == 0 and matrix[nx][ny] == '.':
                        q.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
                        visited[nx][ny] = 1
            else:
                if 0 <= nx < m and 0 <= ny < n:
                    if visited[nx][ny] == 0 and matrix[nx][ny] == '.':
                        q.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
                        visited[nx][ny] = 1

    result = 100000000
    r_x = 0
    r_y = 0
    for i in range(len(dist[-1])):
        if dist[-1][i] != 0:
            if result > dist[-1][i]:
                result = dist[-1][i]
                r_x = len(dist) - 1
                r_y = i

    if result == 100000000:
        result = -1
    
    return [result, r_x, r_y]

matrix = [list(input()) for _ in range(m)]

result = 100000000
a = 0
b = 0
for i in range(m):
    for j in range(n):
        visited = [[0]*n for _ in range(m)]
        dist = [[0]*n for _ in range(m)]

        if matrix[i][j] == 'c':
            temp = bfs(i,j)
            if temp[0] == -1:
                print(-1)
                exit()
            elif result > temp[0]:
                result = temp[0]
                a, b = temp[1], temp[2]
                print(result - (a-i))























