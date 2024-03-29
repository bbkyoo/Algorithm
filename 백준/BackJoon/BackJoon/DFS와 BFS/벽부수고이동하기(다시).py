# 3차원 배열을 만드는데, visit[x][y][i]에서 i가 0이라면 벽을 한번 뚫은 상태이고,
# 1이라면 벽을 뚫을 수 있는 상태를 나타낸다.
# bfs을 돌려주는데 벽을 뚫을 수 있는 상태이고, 벽을 만난다면 벽을 뚫어주고 +1을 해준다.
# 아직 방문하지 않았고 벽이 아니라면 또한 +1을 해준다.

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():  
    q = deque()
    q.append([0,0,1])
    visit = [[[0]*2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1

    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if s[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append([nx,ny,0])
                elif s[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append([nx,ny,w])
    return -1

n ,m = map(int ,input().split())

s = []

for i in range(n):
    s.append(list(map(int, list(input().strip()))))

print(bfs())




# 아래의 백트래킹으로 풀면 시간초과가 나타난다.

# import sys
# from collections import deque
# sys.setrecursionlimit(10 ** 6)
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def bfs():
#     q = deque([])
#     q.append([0,0])
#     visited = [[0]*m for _ in range(n)]
#     visited[0][0] = 1
#     copy = matrix.copy()
#
#     while q:
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if visited[nx][ny] == 0 and copy[nx][ny] == 0:
#                     q.append([nx, ny])
#                     visited[nx][ny] = 1
#                     copy[nx][ny] = copy[x][y] + 1
#
#     return copy[n-1][m-1]
#
# def wallbreak(cnt):
#     global res
#
#     if cnt == 1:
#         res = max(res, bfs())
#
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 1:
#                 matrix[i][j] = 0
#                 wallbreak(cnt+1)
#                 matrix[i][j] = 0
#
# n ,m = map(int ,input().split())
#
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, list(input().strip()))))
#
# res = bfs()
# wallbreak(0)
# if res == 0:
#     print(-1)
# else:
#     print(res+1)