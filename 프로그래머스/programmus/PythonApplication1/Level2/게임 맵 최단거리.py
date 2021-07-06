from collections import deque

def bfs(x, y, maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    dist = [[0]*len(maps[0]) for _ in range(len(maps))]
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]

    q = deque([])
    q.append([x, y])
    dist[x][y] = 1
    visited[x][y] = 1

    while q:
        x, y = q.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

    return dist

def solution(maps):
    answer = bfs(0, 0, maps)
    if answer[-1][-1] == 0:
        return -1
    else:
        return answer[-1][-1]







