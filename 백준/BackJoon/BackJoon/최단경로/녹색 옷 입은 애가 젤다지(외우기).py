# https://pacific-ocean.tistory.com/286

from heapq import heappush, heappop

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 1

def bfs():
    dp = [[100000000] * n for i in range(n)]
    dp[0][0] = s[0][0]
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1

    heap = []
    heappush(heap, [s[0][0], 0, 0])

    while heap:
        z, x, y = heappop(heap)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + s[nx][ny])
                heappush(heap, [dp[nx][ny], nx, ny])
                visited[nx][ny] = 1
    return dp[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break

    s = [] 
    for _ in range(n):
        s.append(list(map(int, input().split())))

    result = bfs()
    print("Problem %d: %d" % (cnt, result))
    cnt += 1