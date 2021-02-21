from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#def bfs_w(x, y):
#    count = 1
#    q = deque()
#    q.append([x,y])
#    visited_w[x][y] = 1
    
#    while q:
#        x, y = q.popleft()

#        for i in range(4):
#            nx = x + dx[i]
#            ny = y + dy[i]

#            if 0 <= nx < m and 0 <= ny < n:
#                if visited_w[nx][ny] == 0 and matrix[nx][ny] == 'W':
#                    q.append([nx, ny])
#                    visited_w[nx][ny] = 1
#                    count += 1

#    return count

#def bfs_b(x, y):
#    count = 1
#    q = deque()
#    q.append([x,y])
#    visited_b[x][y] = 1

#    while q:
#        x, y = q.popleft()

#        for i in range(4):
#            nx = x + dx[i]
#            ny = y + dy[i]

#            if 0 <= nx < m and 0 <= ny < n:
#                if visited_b[nx][ny] == 0 and matrix[nx][ny] == 'B':
#                    q.append([nx, ny])
#                    visited_b[nx][ny] = 1
#                    count += 1
    
#    return count

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == matrix[x][y] and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    count += 1

    return count

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
w_result = 0
b_result = 0

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            count = bfs(i,j)
            if matrix[i][j] == 'W':
                w_result += (count**2)
            else:
                b_result += (count**2)

print(w_result, b_result)












