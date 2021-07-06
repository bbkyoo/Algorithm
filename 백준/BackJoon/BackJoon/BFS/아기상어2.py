from collections import deque

dx = [-1, 1, 0, 0,-1,-1,1,1]
dy = [0, 0, -1, 1,-1,1,-1,1]

def bfs(): 
    while arr:
        x, y = arr.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0:
                    arr.append([nx, ny])
                    matrix[nx][ny] = matrix[x][y] + 1
                
n, m = map(int, input().split())

matrix = []
arr = deque([])

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            arr.append([i, j])
    matrix.append(temp)

bfs()

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, matrix[i][j])

print(result - 1)
