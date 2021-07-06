from collections import deque

def bfs():
    q = deque([])
    q.append([0,0])
    sword = 1000000
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[0][0] = 1
    dist[0][0] = 1

    while q:
        x, y = q.popleft()

        if matrix[x][y] == 2:
            sword = n-1-x + m-1-y + dist[x][y]-1 

        if x == n-1 and y == m-1:
            return min(dist[x][y]-1, sword)
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] != 1 and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

    return sword

n, m, t = map(int, input().split())

matrix = []
visited = [[0]*m for _ in range(n)] 
dist = [[0]*m for _ in range(n)] 

for _ in range(n):
    matrix.append(list(map(int, input().split())))

result = bfs()
if result > t:
    print("Fail")
else:
    print(result)






