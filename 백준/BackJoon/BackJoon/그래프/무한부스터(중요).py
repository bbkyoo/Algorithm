from collections import deque

dx = [1, 0]
dy = [0, 1]

def bfs(x,y,cnt):
    q = deque([])
    q.append([x, y, cnt])
    visited[x][y] = 1
    cnt = 0

    while q:
        x, y, cnt = q.popleft()

        if x == n-1 and y == m-1: 
            return cnt

        for i in range(2):
            for k in range(1, a[x][y]+1):
                nx = x + (dx[i]*k)
                ny = y + (dy[i]*k)

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append([nx ,ny, cnt+1])

n, m = map(int, input().split())

a = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    a.append(list(map(int, input().split())))

print(bfs(0,0,0))