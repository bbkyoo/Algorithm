from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(c_x, c_y, n_x, n_y):
    q = deque()
    q.append([c_x,c_y])
    dist[c_x][c_y] = 1

    while q:
        x, y = q.popleft()
        if x == n_x and y == n_y:
            return dist[x][y] - 1

        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < i and 0 <= ny < i and dist[nx][ny] == 0:
                q.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1

T = int(input())

for _ in range(T):
    i = int(input())
    cur_x , cur_y = map(int, input().split())
    next_x, next_y = map(int, input().split())
    
    dist = [[0]*i for _ in range(i)]

    if cur_x == next_x and cur_y == next_y:
        print(0)
    else:
        result = bfs(cur_x, cur_y, next_x, next_y)
        print(result)