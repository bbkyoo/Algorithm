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