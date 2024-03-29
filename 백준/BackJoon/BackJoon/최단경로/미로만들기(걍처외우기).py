from heapq import heappush, heappop
import sys

def dijkstra(x, y):
    heap = []
    heappush(heap, [0,x,y])
    visited[x][y] = 1

    while True:
        cnt, x, y= heappop(heap)

        if x == n-1 and y == n-1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if s[nx][ny] == 0:
                    s[nx][ny] = 1
                    heappush(heap, [cnt+1, nx, ny])
                else:
                    heappush(heap, [cnt, nx, ny])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

s = []

visited = [[0]*n for _ in range(n)]
for _ in range(n): 
    s.append(list(map(int, input())))

print(dijkstra(0, 0))


# 다른 풀이
# from collections import deque
# 
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]
# 
# def bfs():
#     q = deque([])
#     q.append([0,0])
#     visited[0][0] = 1
# 
#     while q:
#         x, y = q.popleft()
# 
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
# 
#             if 0 <= nx < n and 0 <= ny < n:
#                 if visited[nx][ny] == 0:
#                     if matrix[nx][ny] == 1:
#                         visited[nx][ny] = visited[x][y]
#                         q.appendleft([nx, ny])
#                     else:
#                         visited[nx][ny] = visited[x][y] + 1
#                         q.append([nx, ny])
# 
# n = int(input())
# visited = [[0]*n for _ in range(n)]
# matrix = [list(map(int, input())) for _ in range(n)]
# bfs()
# print(visited[-1][-1]-1)
