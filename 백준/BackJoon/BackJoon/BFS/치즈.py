from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    global left

    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == 0:
                    if cheese[nx][ny] == 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                    else:
                        cheese[nx][ny] = 2
                        visited[nx][ny] = 1
                        left -= 1

def delete():
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 2:
                cheese[i][j] = 0


n, m = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(n)]

left = 0
for i in range(n):
    for j in range(m):
        if cheese[i][j] == 1:
            left += 1

count = 0
temp = left

while left != 0:
    visited = [[0]*m for _ in range(n)]
    bfs(0, 0)
    if left != 0:
        temp = left

    count += 1
    delete()
   
print(count)
print(temp)    





